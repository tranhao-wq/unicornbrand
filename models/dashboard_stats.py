from database import db
from datetime import datetime

class DashboardStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    total_users = db.Column(db.Integer)
    total_products = db.Column(db.Integer)
    total_orders = db.Column(db.Integer)
    total_revenue = db.Column(db.Float)
    revenue_by_month = db.Column(db.JSON)
    users_by_month = db.Column(db.JSON)
    status_counts = db.Column(db.JSON)
    top_products = db.Column(db.JSON)
    cat_counts = db.Column(db.JSON) 