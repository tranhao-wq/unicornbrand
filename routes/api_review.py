from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models.review import Review
from database import db

api_review = Blueprint('api_review', __name__)

@api_review.route('/api/reviews/<int:product_id>', methods=['GET'])
def get_reviews(product_id):
    reviews = Review.query.filter_by(product_id=product_id).all()
    return jsonify([
        {
            'id': r.id,
            'user_id': r.user_id,
            'username': r.user.get_full_name() if hasattr(r.user, 'get_full_name') else '',
            'rating': r.rating,
            'comment': r.comment,
            'created_at': r.created_at.strftime('%Y-%m-%d %H:%M')
        } for r in reviews
    ])

@api_review.route('/api/reviews/add', methods=['POST'])
@login_required
def add_review():
    data = request.get_json()
    product_id = data.get('product_id')
    rating = data.get('rating')
    comment = data.get('comment', '')
    # Kiểm tra user đã review chưa (1 user chỉ review 1 lần/1 sản phẩm)
    if Review.query.filter_by(user_id=current_user.id, product_id=product_id).first():
        return jsonify({'success': False, 'message': 'You have already reviewed this product.'}), 400
    review = Review(user_id=current_user.id, product_id=product_id, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()
    return jsonify({'success': True})

@api_review.route('/api/reviews/delete', methods=['POST'])
@login_required
def delete_review():
    data = request.get_json()
    review_id = data.get('review_id')
    review = Review.query.filter_by(id=review_id, user_id=current_user.id).first()
    if review:
        db.session.delete(review)
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False}), 404 