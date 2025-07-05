from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from functools import wraps
from models.user import User
from models.product import Product
from models.order import Order, OrderItem, ORDER_STATUS_PENDING, ORDER_STATUS_CONFIRMED, ORDER_STATUS_SHIPPED, ORDER_STATUS_DELIVERED, ORDER_STATUS_CANCELLED
from forms.product_forms import ProductForm
from database import db
from flask_socketio import SocketIO, emit
from flask import current_app
from werkzeug.utils import secure_filename
import os
import io
from sqlalchemy import extract, func
from collections import Counter
from datetime import datetime, timedelta
from models.dashboard_stats import DashboardStats
from routes.main import get_supabase_client, get_signed_image_url # Import from main_bp
import logging

admin_bp = Blueprint('admin', __name__)

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
SUPABASE_BUCKET = 'product-images'

# Configure logging
logger = logging.getLogger(__name__)

def upload_image_to_supabase(file_storage):
    supabase = get_supabase_client()
    if not supabase:
        logger.error("Supabase client not available for image upload.")
        return None

    file_data = file_storage.read()
    file_name = secure_filename(file_storage.filename)
    unique_name = f"{int(datetime.utcnow().timestamp())}_{file_name}"
    try:
        supabase.storage.from_(SUPABASE_BUCKET).upload(unique_name, io.BytesIO(file_data))
        return unique_name
    except Exception as e:
        logger.error(f"Error uploading image {file_name} to Supabase: {e}")
        return None

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Access denied. Admin privileges required.', 'error')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    # Get statistics
    total_users, total_products, total_orders, total_revenue = _get_basic_stats()
    pending_orders = Order.query.filter_by(status=ORDER_STATUS_PENDING).count()

    # Recent orders
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()
    # Low stock products
    low_stock_products = Product.query.filter(Product.stock_quantity <= 5).all()

    now = datetime.utcnow()
    months = [(now - timedelta(days=30*i)).strftime('%Y-%m') for i in range(5, -1, -1)]
    
    revenue_by_month = _get_monthly_revenue(months)
    users_by_month = _get_monthly_new_users(months)
    status_labels, status_counts = _get_order_status_distribution()
    top_products_data = _get_top_selling_products()
    cat_counts_data = _get_product_category_distribution()

    top_product_names = [p['name'] for p in top_products_data]
    top_product_qtys = [p['qty'] for p in top_products_data]
    cat_labels = [c['category'] for c in cat_counts_data]
    cat_values = [c['count'] for c in cat_counts_data]

    return render_template('admin/dashboard.html',
                         total_users=total_users,
                         total_products=total_products,
                         total_orders=total_orders,
                         pending_orders=pending_orders,
                         total_revenue=total_revenue,
                         recent_orders=recent_orders,
                         low_stock_products=low_stock_products,
                         months=months,
                         revenue_by_month=revenue_by_month,
                         users_by_month=users_by_month,
                         status_labels=status_labels,
                         status_counts=status_counts,
                         top_product_names=top_product_names,
                         top_product_qtys=top_product_qtys,
                         cat_labels=cat_labels,
                         cat_values=cat_values
    )

@admin_bp.route('/products')
@login_required
@admin_required
def products():
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(
        page=page, per_page=10, error_out=False
    )
    return render_template('admin/products.html', products=products)

@admin_bp.route('/products/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        image_url = None
        if form.image.data:
            image_url = upload_image_to_supabase(form.image.data)
        product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            category=form.category.data,
            brand=form.brand.data,
            image_url=image_url,
            stock_quantity=form.stock_quantity.data,
            sizes=form.sizes.data,
            colors=form.colors.data,
            is_active=form.is_active.data
        )
        db.session.add(product)
        db.session.commit()
        socketio = current_app.extensions.get('socketio')
        if socketio:
            socketio.emit('product_update', {'action': 'add', 'product_id': product.id})
        flash('Product added successfully!', 'success')
        update_dashboard_stats()
        return redirect(url_for('admin.products'))
    return render_template('admin/product_form.html', form=form, title='Add Product', product=None)

@admin_bp.route('/products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_product(id):
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        if form.image.data:
            image_url = upload_image_to_supabase(form.image.data)
            product.image_url = image_url
        form.populate_obj(product)
        db.session.commit()
        socketio = current_app.extensions.get('socketio')
        if socketio:
            socketio.emit('product_update', {'action': 'edit', 'product_id': product.id})
        flash('Product updated successfully!', 'success')
        update_dashboard_stats()
        return redirect(url_for('admin.products'))
    return render_template('admin/product_form.html', form=form, title='Edit Product', product=product)

@admin_bp.route('/products/delete/<int:id>')
@login_required
@admin_required
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    # Emit realtime event
    socketio = current_app.extensions.get('socketio')
    if socketio:
        socketio.emit('product_update', {'action': 'delete', 'product_id': id})
    flash('Product deleted successfully!', 'success')
    update_dashboard_stats()
    return redirect(url_for('admin.products'))

@admin_bp.route('/orders')
@login_required
@admin_required
def orders():
    page = request.args.get('page', 1, type=int)
    status_filter = request.args.get('status', '')
    
    query = Order.query
    if status_filter:
        query = query.filter_by(status=status_filter)
    
    orders = query.order_by(Order.created_at.desc()).paginate(
        page=page, per_page=10, error_out=False
    )
    return render_template('admin/orders.html', orders=orders, status_filter=status_filter)

@admin_bp.route('/orders/<int:id>')
@login_required
@admin_required
def order_detail(id):
    order = Order.query.get_or_404(id)
    return render_template('admin/order_detail.html', order=order)

@admin_bp.route('/orders/update_status/<int:id>', methods=['POST'])
@login_required
@admin_required
def update_order_status(id):
    order = Order.query.get_or_404(id)
    new_status = request.form.get('status')
    
    if new_status in [ORDER_STATUS_PENDING, ORDER_STATUS_CONFIRMED, ORDER_STATUS_SHIPPED, ORDER_STATUS_DELIVERED, ORDER_STATUS_CANCELLED]:
        order.status = new_status
        db.session.commit()
        flash(f'Order #{order.id} status updated to {new_status}!', 'success')
    else:
        flash('Invalid status!', 'error')
    
    update_dashboard_stats()
    return redirect(url_for('admin.order_detail', id=id))

@admin_bp.route('/users')
@login_required
@admin_required
def users():
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(
        page=page, per_page=10, error_out=False
    )
    return render_template('admin/users.html', users=users)

def _get_basic_stats():
    total_users = User.query.count()
    total_products = Product.query.count()
    total_orders = Order.query.count()
    total_revenue = db.session.query(func.sum(Order.total_amount)).filter(Order.status=='delivered').scalar() or 0
    return total_users, total_products, total_orders, total_revenue

def _get_monthly_revenue(months):
    revenue_by_month = []
    for m in months:
        year, month = map(int, m.split('-'))
        total = db.session.query(func.sum(Order.total_amount)).filter(
            extract('year', Order.created_at) == year,
            extract('month', Order.created_at) == month,
            Order.status == 'delivered'
        ).scalar() or 0
        revenue_by_month.append(total)
    return revenue_by_month

def _get_monthly_new_users(months):
    users_by_month = []
    for m in months:
        year, month = map(int, m.split('-'))
        count = User.query.filter(
            extract('year', User.created_at) == year,
            extract('month', User.created_at) == month
        ).count()
        users_by_month.append(count)
    return users_by_month

def _get_order_status_distribution():
    status_labels = [ORDER_STATUS_PENDING, ORDER_STATUS_CONFIRMED, ORDER_STATUS_SHIPPED, ORDER_STATUS_DELIVERED, ORDER_STATUS_CANCELLED]
    status_counts = [Order.query.filter_by(status=s).count() for s in status_labels]
    return status_labels, status_counts

def _get_top_selling_products():
    top_products = db.session.query(
        Product.name, func.sum(OrderItem.quantity).label('qty')
    ).join(OrderItem).join(Order).filter(Order.status=='delivered').group_by(Product.name).order_by(func.sum(OrderItem.quantity).desc()).limit(5).all()
    top_products_data = [{'name': p[0], 'qty': p[1]} for p in top_products]
    return top_products_data

def _get_product_category_distribution():
    cat_counts = db.session.query(Product.category, func.count(Product.id)).group_by(Product.category).all()
    cat_counts_data = [{'category': c[0], 'count': c[1]} for c in cat_counts]
    return cat_counts_data

def update_dashboard_stats():
    db.session.expire_all()
    
    total_users, total_products, total_orders, total_revenue = _get_basic_stats()
    
    now = datetime.utcnow()
    months = [(now - timedelta(days=30*i)).strftime('%Y-%m') for i in range(5, -1, -1)]
    
    revenue_by_month = _get_monthly_revenue(months)
    users_by_month = _get_monthly_new_users(months)
    status_labels, status_counts = _get_order_status_distribution()
    top_products_data = _get_top_selling_products()
    cat_counts_data = _get_product_category_distribution()
    
    # Save or update
    stats = DashboardStats.query.first()
    if not stats:
        stats = DashboardStats()
        db.session.add(stats)
    stats.total_users = total_users
    stats.total_products = total_products
    stats.total_orders = total_orders
    stats.total_revenue = total_revenue
    stats.revenue_by_month = revenue_by_month
    stats.users_by_month = users_by_month
    stats.status_counts = status_counts
    stats.top_products = top_products_data
    stats.cat_counts = cat_counts_data
    db.session.commit()