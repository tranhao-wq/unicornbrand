from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models.address import Address
from database import db

api_address = Blueprint('api_address', __name__)

@api_address.route('/api/addresses', methods=['GET'])
@login_required
def get_addresses():
    addresses = Address.query.filter_by(user_id=current_user.id).all()
    return jsonify([
        {
            'id': a.id,
            'recipient_name': a.recipient_name,
            'phone': a.phone,
            'address_line': a.address_line,
            'city': a.city,
            'district': a.district,
            'ward': a.ward,
            'is_default': a.is_default
        } for a in addresses
    ])

@api_address.route('/api/addresses/add', methods=['POST'])
@login_required
def add_address():
    data = request.get_json()
    address = Address(
        user_id=current_user.id,
        recipient_name=data.get('recipient_name'),
        phone=data.get('phone'),
        address_line=data.get('address_line'),
        city=data.get('city'),
        district=data.get('district'),
        ward=data.get('ward'),
        is_default=data.get('is_default', False)
    )
    if address.is_default:
        Address.query.filter_by(user_id=current_user.id, is_default=True).update({'is_default': False})
    db.session.add(address)
    db.session.commit()
    return jsonify({'success': True})

@api_address.route('/api/addresses/delete', methods=['POST'])
@login_required
def delete_address():
    data = request.get_json()
    address_id = data.get('address_id')
    address = Address.query.filter_by(id=address_id, user_id=current_user.id).first()
    if address:
        db.session.delete(address)
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False}), 404 