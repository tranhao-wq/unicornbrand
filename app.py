from flask import Flask, render_template
from config import Config
from database import db, login_manager, migrate
import os
from flask_socketio import SocketIO
from flask_compress import Compress
from flask_caching import Cache

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Bandwidth optimization
    Compress(app)  # Gzip compression - reduces response size by 70%
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})
    
    # Static files caching
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # 1 year
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    migrate.init_app(app, db)

    # SocketIO
    socketio = SocketIO(app)
    
    # Register blueprints
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.admin import admin_bp
    from routes.cart import cart_bp
    from routes.api_cart import api_cart
    from routes.payment import payment_bp
    from routes.api_wishlist import api_wishlist
    from routes.api_review import api_review
    from routes.api_address import api_address
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(api_cart)
    app.register_blueprint(payment_bp)
    app.register_blueprint(api_wishlist)
    app.register_blueprint(api_review)
    app.register_blueprint(api_address)
    
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

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    return app, socketio


if __name__ == '__main__':
    app, socketio = create_app()
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)