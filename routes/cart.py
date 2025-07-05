from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import login_required, current_user
from models.product import Product
from models.order import Order, OrderItem
from models.cart_item import CartItem
from database import db

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add', methods=['POST'])
@login_required
def add_to_cart():
    product_id = request.form.get('product_id', type=int)
    quantity = request.form.get('quantity', 1, type=int)
    size = request.form.get('size')
    color = request.form.get('color')
    
    product = Product.query.get_or_404(product_id)
    
    if not product.is_in_stock():
        flash('Product is out of stock', 'error')
        return redirect(url_for('main.product_detail', id=product_id))
    
    # Initialize cart in session if not exists
    if 'cart' not in session:
        session['cart'] = []
    
    # Check if item already in cart
    cart_item = None
    for item in session['cart']:
        if (item['product_id'] == product_id and 
            item['size'] == size and 
            item['color'] == color):
            cart_item = item
            break
    
    if cart_item:
        cart_item['quantity'] += quantity
    else:
        session['cart'].append({
            'product_id': product_id,
            'quantity': quantity,
            'size': size,
            'color': color,
            'name': product.name,
            'price': product.price,
            'image_url': product.image_url
        })
    
    session.modified = True
    flash(f'{product.name} added to cart!', 'success')
    return redirect(url_for('main.product_detail', id=product_id))

@cart_bp.route('/view')
@login_required
def view_cart():
    # Lấy cart từ DB (CartItem)
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    # Tạo list dict để render template
    items = []
    total = 0
    for item in cart_items:
        product = Product.query.get(item.product_id)
        if not product:
            continue
        item_dict = {
            'product_id': item.product_id,
            'quantity': item.quantity,
            'size': item.size,
            'color': item.color,
            'name': product.name,
            'price': product.price,
            'image_url': product.image_url
        }
        items.append(item_dict)
        total += product.price * item.quantity
    return render_template('cart/view.html', cart_items=items, total=total)

@cart_bp.route('/update', methods=['POST'])
@login_required
def update_cart():
    cart_index = request.form.get('cart_index', type=int)
    quantity = request.form.get('quantity', 1, type=int)
    
    if 'cart' in session and 0 <= cart_index < len(session['cart']):
        if quantity > 0:
            session['cart'][cart_index]['quantity'] = quantity
        else:
            session['cart'].pop(cart_index)
        session.modified = True
        flash('Cart updated!', 'success')
    
    return redirect(url_for('cart.view_cart'))

@cart_bp.route('/remove/<int:cart_index>')
@login_required
def remove_from_cart(cart_index):
    if 'cart' in session and 0 <= cart_index < len(session['cart']):
        removed_item = session['cart'].pop(cart_index)
        session.modified = True
        flash(f'{removed_item["name"]} removed from cart!', 'info')
    
    return redirect(url_for('cart.view_cart'))

@cart_bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart_items = session.get('cart', [])
    if not cart_items:
        flash('Your cart is empty!', 'error')
        return redirect(url_for('main.products'))
    
    if request.method == 'POST':
        shipping_address = request.form.get('shipping_address')
        phone = request.form.get('phone')
        notes = request.form.get('notes', '')
        
        if not shipping_address:
            flash('Shipping address is required!', 'error')
            return render_template('cart/checkout.html', cart_items=cart_items)
        
        # Calculate total
        total = sum(item['price'] * item['quantity'] for item in cart_items)
        
        # Create order
        order = Order(
            user_id=current_user.id,
            total_amount=total,
            shipping_address=shipping_address,
            phone=phone,
            notes=notes
        )
        db.session.add(order)
        db.session.flush()  # Get order ID
        
        # Create order items
        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item['product_id'],
                quantity=item['quantity'],
                price=item['price'],
                size=item['size'],
                color=item['color']
            )
            db.session.add(order_item)
        
        db.session.commit()
        
        # Clear cart
        session.pop('cart', None)
        
        flash(f'Order #{order.id} placed successfully!', 'success')
        return redirect(url_for('auth.orders'))
    
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart/checkout.html', cart_items=cart_items, total=total)