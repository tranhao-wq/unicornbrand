from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models.wishlist import WishlistItem
from database import db

api_wishlist = Blueprint('api_wishlist', __name__)

@api_wishlist.route('/api/wishlist', methods=['GET'])
@login_required
def get_wishlist():
    items = WishlistItem.query.filter_by(user_id=current_user.id).all()
    return jsonify([{'product_id': i.product_id} for i in items])

@api_wishlist.route('/api/wishlist/add', methods=['POST'])
@login_required
def add_to_wishlist():
    data = request.get_json()
    product_id = data.get('product_id')
    if not WishlistItem.query.filter_by(user_id=current_user.id, product_id=product_id).first():
        db.session.add(WishlistItem(user_id=current_user.id, product_id=product_id))
        db.session.commit()
    return jsonify({'success': True})

@api_wishlist.route('/api/wishlist/remove', methods=['POST'])
@login_required
def remove_from_wishlist():
    data = request.get_json()
    product_id = data.get('product_id')
    item = WishlistItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
    return jsonify({'success': True}) 