from flask import Flask, render_template
from config import Config
from database import db, login_manager, migrate
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    migrate.init_app(app, db)
    
    # Register blueprints
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.admin import admin_bp
    from routes.cart import cart_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    
    # Create tables
    with app.app_context():
        db.create_all()

    # Add Privacy Policy and Terms of Service routes
    @app.route('/privacy_policy')
    def privacy_policy():
        return render_template('privacy_policy.html')

    @app.route('/terms_of_service')
    def terms_of_service():
        return render_template('terms_of_service.html')

    # Add Shipping Info, Returns, Size Guide routes
    @app.route('/shipping_info')
    def shipping_info():
        return render_template('shipping_info.html')

    @app.route('/returns')
    def returns():
        return render_template('returns.html')

    @app.route('/size_guide')
    def size_guide():
        return render_template('size_guide.html')

    return app


if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)