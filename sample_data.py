from app import create_app
from database import db
from models.user import User
from models.product import Product

def create_sample_data():
    app = create_app()
    with app.app_context():
        # Create sample products
        products = [
            {
                'name': 'Air Max Classic',
                'description': 'Comfortable running shoes with excellent cushioning and breathable design.',
                'price': 129.99,
                'category': 'sneakers',
                'image_url': 'https://via.placeholder.com/400x300/667eea/ffffff?text=Air+Max+Classic',
                'stock_quantity': 25,
                'sizes': '6,7,8,9,10,11,12',
                'colors': 'Black,White,Red,Blue'
            },
            {
                'name': 'Urban Walker Boots',
                'description': 'Stylish leather boots perfect for city adventures and casual wear.',
                'price': 189.99,
                'category': 'boots',
                'image_url': 'https://via.placeholder.com/400x300/764ba2/ffffff?text=Urban+Walker',
                'stock_quantity': 15,
                'sizes': '7,8,9,10,11,12',
                'colors': 'Brown,Black,Tan'
            },
            {
                'name': 'Executive Oxford',
                'description': 'Premium leather dress shoes for professional and formal occasions.',
                'price': 249.99,
                'category': 'formal',
                'image_url': 'https://via.placeholder.com/400x300/1f2937/ffffff?text=Executive+Oxford',
                'stock_quantity': 12,
                'sizes': '7,8,9,10,11,12',
                'colors': 'Black,Brown'
            },
            {
                'name': 'Sport Pro Runner',
                'description': 'High-performance athletic shoes designed for serious runners.',
                'price': 159.99,
                'category': 'sports',
                'image_url': 'https://via.placeholder.com/400x300/10b981/ffffff?text=Sport+Pro',
                'stock_quantity': 30,
                'sizes': '6,7,8,9,10,11,12,13',
                'colors': 'White,Black,Blue,Green'
            },
            {
                'name': 'Comfort Casual',
                'description': 'Everyday casual shoes that provide all-day comfort and style.',
                'price': 89.99,
                'category': 'casual',
                'image_url': 'https://via.placeholder.com/400x300/f59e0b/ffffff?text=Comfort+Casual',
                'stock_quantity': 20,
                'sizes': '6,7,8,9,10,11,12',
                'colors': 'Gray,Navy,White,Beige'
            },
            {
                'name': 'Summer Breeze Sandals',
                'description': 'Lightweight and comfortable sandals perfect for warm weather.',
                'price': 69.99,
                'category': 'sandals',
                'image_url': 'https://via.placeholder.com/400x300/ef4444/ffffff?text=Summer+Breeze',
                'stock_quantity': 18,
                'sizes': '6,7,8,9,10,11,12',
                'colors': 'Brown,Black,White'
            },
            {
                'name': 'Trail Master Hiking',
                'description': 'Durable hiking boots built for outdoor adventures and rough terrain.',
                'price': 199.99,
                'category': 'boots',
                'image_url': 'https://via.placeholder.com/400x300/8b5cf6/ffffff?text=Trail+Master',
                'stock_quantity': 10,
                'sizes': '7,8,9,10,11,12,13',
                'colors': 'Brown,Green,Black'
            },
            {
                'name': 'Street Style Sneakers',
                'description': 'Trendy sneakers that combine street fashion with everyday comfort.',
                'price': 109.99,
                'category': 'sneakers',
                'image_url': 'https://via.placeholder.com/400x300/06b6d4/ffffff?text=Street+Style',
                'stock_quantity': 22,
                'sizes': '6,7,8,9,10,11,12',
                'colors': 'White,Black,Red,Yellow'
            }
        ]
        
        for product_data in products:
            existing_product = Product.query.filter_by(name=product_data['name']).first()
            if not existing_product:
                product = Product(**product_data)
                db.session.add(product)
        
        # Create sample customer user
        customer = User.query.filter_by(email='customer@example.com').first()
        if not customer:
            customer = User(
                username='customer',
                email='customer@example.com',
                first_name='John',
                last_name='Doe',
                phone='(555) 123-4567',
                address='456 Customer Lane, User City, UC 67890'
            )
            customer.set_password('customer123')
            db.session.add(customer)
        
        db.session.commit()
        print("Sample data created successfully!")
        print("Admin login: admin@unicornbrand.com / admin123")
        print("Customer login: customer@example.com / customer123")

if __name__ == '__main__':
    create_sample_data()