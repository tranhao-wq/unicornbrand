from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from database import db

# Order Status Constants
ORDER_STATUS_PENDING = 'pending'
ORDER_STATUS_CONFIRMED = 'confirmed'
ORDER_STATUS_SHIPPED = 'shipped'
ORDER_STATUS_DELIVERED = 'delivered'
ORDER_STATUS_CANCELLED = 'cancelled'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default=ORDER_STATUS_PENDING)
    shipping_address = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(20))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    items = db.relationship('OrderItem', backref='order', lazy=True, cascade='all, delete-orphan')
    
    def get_status_badge_class(self):
        status_classes = {
            ORDER_STATUS_PENDING: 'bg-yellow-100 text-yellow-800',
            ORDER_STATUS_CONFIRMED: 'bg-blue-100 text-blue-800',
            ORDER_STATUS_SHIPPED: 'bg-purple-100 text-purple-800',
            ORDER_STATUS_DELIVERED: 'bg-green-100 text-green-800',
            ORDER_STATUS_CANCELLED: 'bg-red-100 text-red-800'
        }
        return status_classes.get(self.status, 'bg-gray-100 text-gray-800')
    
    def get_total_items(self):
        return sum(item.quantity for item in self.items)
    
    def __repr__(self):
        return f'<Order {self.id}>'

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)  # Price at time of order
    size = db.Column(db.String(10))
    color = db.Column(db.String(20))
    
    def get_subtotal(self):
        return self.quantity * self.price
    
    def __repr__(self):
        return f'<OrderItem {self.id}>'