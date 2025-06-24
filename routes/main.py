from flask import Blueprint, render_template, request, jsonify
from models.product import Product
from forms.product_forms import SearchForm
from sqlalchemy import or_

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Get featured products (latest 8 products)
    featured_products = Product.query.filter_by(is_active=True).order_by(Product.created_at.desc()).limit(8).all()
    
    # Get products by category for showcase
    categories = ['sneakers', 'boots', 'formal', 'sports']
    category_products = {}
    for category in categories:
        category_products[category] = Product.query.filter_by(category=category, is_active=True).limit(4).all()
    
    return render_template('index.html', 
                         featured_products=featured_products,
                         category_products=category_products)

@main_bp.route('/products')
def products():
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
    per_page = 12
    
    query = Product.query.filter_by(is_active=True)
    
    # Apply filters
    search_query = request.args.get('query', '')
    category = request.args.get('category', '')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    
    if search_query:
        query = query.filter(or_(
            Product.name.contains(search_query),
            Product.description.contains(search_query),
            Product.brand.contains(search_query)
        ))
    
    if category:
        query = query.filter_by(category=category)
    
    if min_price:
        query = query.filter(Product.price >= min_price)
    
    if max_price:
        query = query.filter(Product.price <= max_price)
    
    products = query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('products.html', 
                         products=products, 
                         form=form,
                         search_query=search_query,
                         category=category)

@main_bp.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    related_products = Product.query.filter(
        Product.category == product.category,
        Product.id != product.id,
        Product.is_active == True
    ).limit(4).all()
    
    return render_template('product_detail.html', 
                         product=product,
                         related_products=related_products)

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')