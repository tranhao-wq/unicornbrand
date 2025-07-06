from flask import Flask
from flask_compress import Compress
from flask_caching import Cache

def create_app():
    app = Flask(__name__)
    
    # Compression - giảm 70% dung lượng response
    Compress(app)
    
    # Caching - giảm database queries
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})
    
    # Static files caching
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # 1 year
    
    return app, cache