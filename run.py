#!/usr/bin/env python3
"""
UNICORN BRAND E-commerce Application
Run script for development and production
"""

from app import create_app
import os

if __name__ == '__main__':
    app = create_app()
    
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the application
    app.run(
        host='0.0.0.0',
        port=port,
        debug=os.environ.get('FLASK_ENV') == 'development'
    )