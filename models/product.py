from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import current_app

from database import db

DEFAULT_BRAND = 'UNICORN BRAND'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), default=DEFAULT_BRAND)
    image_url = db.Column(db.String(200))
    stock_quantity = db.Column(db.Integer, default=0)
    sizes = db.Column(db.String(100))  # JSON string: "6,7,8,9,10,11,12"
    colors = db.Column(db.String(100))  # JSON string: "Black,White,Red"
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    order_items = db.relationship('OrderItem', backref='product', lazy=True)
    
    def get_sizes_list(self):
        return self.sizes.split(',') if self.sizes else []
    
    def get_colors_list(self):
        return self.colors.split(',') if self.colors else []
    
    def is_in_stock(self):
        return self.stock_quantity > 0
    
    def formatted_price(self):
        return f"${self.price:.2f}"
    
    def get_image_url(self):
        if not self.image_url:
            return None
        if self.image_url.startswith('http'):
            return self.image_url
        return current_app.config.get('SUPABASE_URL', '') + self.image_url
    
    def __repr__(self):
        return f'<Product {self.name}>'