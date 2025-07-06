from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import db, Product, CartItem  # CartItem sẽ tạo nếu chưa có

api_cart = Blueprint('api_cart', __name__)

# Helper: get or create cart item
def get_or_create_cart_item(user_id, product_id, size=None, color=None):
    item = CartItem.query.filter_by(user_id=user_id, product_id=product_id, size=size, color=color).first()
    if not item:
        item = CartItem(user_id=user_id, product_id=product_id, size=size, color=color, quantity=0)
        db.session.add(item)
    return item

@api_cart.route('/api/cart/add', methods=['POST'])
@login_required
def add_to_cart_api():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = int(data.get('quantity', 1))
    size = data.get('size')
    color = data.get('color')
    product = Product.query.get(product_id)
    if not product or not product.is_in_stock:
        return jsonify({'success': False, 'message': 'Product not available'}), 400
    item = get_or_create_cart_item(current_user.id, product_id, size, color)
    item.quantity += quantity
    db.session.commit()
    return jsonify({'success': True, 'cart_count': get_cart_count(current_user.id)})

@api_cart.route('/api/cart/count', methods=['GET'])
@login_required
def cart_count_api():
    return jsonify({'cart_count': get_cart_count(current_user.id)})

def get_cart_count(user_id):
    return sum(item.quantity for item in CartItem.query.filter_by(user_id=user_id).all())

@api_cart.route('/api/cart', methods=['GET'])
@login_required
def get_cart_api():
    items = CartItem.query.filter_by(user_id=current_user.id).all()
    result = []
    for item in items:
        result.append({
            'product_id': item.product_id,
            'quantity': item.quantity,
            'size': item.size,
            'color': item.color
        })
    return jsonify({'cart': result})

@api_cart.route('/api/cart/remove', methods=['DELETE'])
@login_required
def remove_from_cart_api():
    data = request.get_json()
    product_id = data.get('product_id')
    size = data.get('size')
    color = data.get('color')
    item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id, size=size, color=color).first()
    if item:
        db.session.delete(item)
        db.session.commit()
    return jsonify({'success': True, 'cart_count': get_cart_count(current_user.id)})

@api_cart.route('/api/cart/sync', methods=['POST'])
@login_required
def sync_cart_api():
    data = request.get_json()
    cart = data.get('cart', {})
    # Xóa cart cũ
    CartItem.query.filter_by(user_id=current_user.id).delete()
    # Thêm lại từ localStorage
    for product_id, item in cart.items():
        if not isinstance(item, dict):
            app.logger.warning(f"Invalid cart item: {item}")
            continue
        quantity = int(item.get('quantity', 1))
        size = item.get('size')
        color = item.get('color')
        db.session.add(CartItem(user_id=current_user.id, product_id=product_id, quantity=quantity, size=size, color=color))
    db.session.commit()
    return jsonify({'success': True, 'cart_count': get_cart_count(current_user.id)}) 