from flask import Blueprint, render_template, request, jsonify
from models.product import Product
from forms.product_forms import SearchForm, PRODUCT_CATEGORIES
from sqlalchemy import or_
import os
import logging

main_bp = Blueprint('main', __name__)

SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
SUPABASE_BUCKET = 'product-images'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_supabase_client():
    """Initializes and returns a Supabase client."""
    if not SUPABASE_URL or not SUPABASE_KEY:
        logger.error("Supabase URL or Key not configured.")
        return None
    try:
        from supabase import create_client, Client
        return create_client(SUPABASE_URL, SUPABASE_KEY)
    except Exception as e:
        logger.error(f"Error initializing Supabase client: {e}")
        return None

def get_signed_image_url(supabase_client, image_path):
    """Generates a signed URL for a given image path from Supabase storage."""
    if not supabase_client or not image_path:
        return None
    try:
        res = supabase_client.storage.from_(SUPABASE_BUCKET).create_signed_url(image_path, 3600)
        signed_url = res.get('signedURL')
        if not signed_url:
            return None
        if signed_url.startswith('http'):
            return signed_url
        return SUPABASE_URL + signed_url
    except Exception as e:
        logger.error(f"Error generating signed URL for {image_path}: {e}")
        return None

@main_bp.route('/')
def index():
    supabase = get_supabase_client()
    # Get featured products (latest 8 products)
    featured_products = Product.query.filter_by(is_active=True).order_by(Product.created_at.desc()).limit(8).all()
    
    # Get products by category for showcase
    category_products = {}
    for category_tuple in PRODUCT_CATEGORIES:
        category_slug = category_tuple[0]
        category_products[category_slug] = Product.query.filter_by(category=category_slug, is_active=True).limit(4).all()
    
    return render_template('index.html', 
                         featured_products=featured_products,
                         category_products=category_products)

@main_bp.route('/products')
def products():
    supabase = get_supabase_client()
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
        signed_url = get_signed_image_url(supabase, p.image_url) if p.image_url else None
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
            'is_in_stock': p.is_in_stock(),
            'get_image_url': lambda: signed_url
        })
    # Tạo đối tượng phân trang mới cho template
    class DummyPagination(type(products)):
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
    supabase = get_supabase_client()
    product = Product.query.get_or_404(id)
    
    # Get signed URL for the product image
    if product.image_url:
        product.image_url = get_signed_image_url(supabase, product.image_url)

    related_products = Product.query.filter(
        Product.category == product.category,
        Product.id != product.id,
        Product.is_active == True
    ).limit(4).all()
    
    # Get signed URLs for related products
    for p in related_products:
        if p.image_url:
            p.image_url = get_signed_image_url(supabase, p.image_url)

    return render_template('product_detail.html', 
                         product=product,
                         related_products=related_products)

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')