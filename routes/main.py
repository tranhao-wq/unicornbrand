from flask import Blueprint, render_template, request, jsonify
from models.product import Product
from forms.product_forms import SearchForm
from sqlalchemy import or_
from supabase import create_client, Client
import os

main_bp = Blueprint('main', __name__)

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
SUPABASE_BUCKET = 'product-images'

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
    
    # Sinh signed URL cho ảnh
    product_items = []
    seen_ids = set()
    for p in products.items:
        if p.id in seen_ids:
            continue  # Bỏ qua sản phẩm trùng id
        seen_ids.add(p.id)
        signed_url = None
        if p.image_url:
            try:
                res = supabase.storage.from_(SUPABASE_BUCKET).create_signed_url(p.image_url.split('/')[-1], 3600)
                signed_url = SUPABASE_URL + res.get('signedURL') if res.get('signedURL') else None
            except Exception:
                signed_url = None  # Nếu lỗi (file không tồn tại), dùng placeholder
        product_items.append({
            'id': p.id,
            'name': p.name,
            'category': p.category,
            'description': p.description,
            'brand': p.brand,
            'image_url': signed_url,
            'stock_quantity': p.stock_quantity,
            'is_active': p.is_active,
            'price': p.price,
            'formatted_price': p.formatted_price(),
            'is_in_stock': p.is_in_stock()
        })
    # Tạo đối tượng phân trang mới cho template
    from flask_sqlalchemy import Pagination
    class DummyPagination:
        def __init__(self, orig, items):
            self.__dict__.update(orig.__dict__)
            self.items = items
    products_for_template = DummyPagination(products, product_items)
    return render_template('products.html', 
                         products=products_for_template, 
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