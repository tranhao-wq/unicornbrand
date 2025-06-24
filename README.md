# UNICORN BRAND - E-commerce Web Application

A professional, production-ready Python-based fullstack web application for a shoe e-commerce site.
<<<<<<< HEAD
=======
## Pics
>>>>>>> 768236fb01da289b1159d2e59cef09923f6b8059

## Features

### 🛍️ Core Functionality
- **Product Catalog**: Browse shoes with images, prices, descriptions, and filters
- **Shopping Cart**: Add items, manage quantities, and checkout
- **User Authentication**: Secure signup, login, logout, and profile management
- **Order Management**: Track orders with status updates
- **Admin Dashboard**: Complete CRUD operations for products, orders, and users

### 🔍 Advanced Features
- **Search & Filters**: Find products by name, category, price range
- **Responsive Design**: Mobile-first approach with professional UI/UX
- **Session Management**: Persistent shopping cart across sessions
- **Role-based Access**: Admin and customer user roles
- **Order Tracking**: Complete order lifecycle management

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite (easily configurable to PostgreSQL)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with modern design principles
- **Authentication**: Flask-Login with secure password hashing
- **Forms**: Flask-WTF with validation

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Quick Start

1. **Clone and navigate to the project**:
   ```bash
   cd unicorn_brand
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   
   # Windows
   venv\\Scripts\\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   - Open browser to `http://localhost:5000`
   - Admin login: `admin@unicornbrand.com` / `admin123`

## Project Structure

```
unicorn_brand/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── models/              # Database models
│   ├── user.py          # User model with authentication
│   ├── product.py       # Product model with inventory
│   └── order.py         # Order and OrderItem models
├── routes/              # Application routes (blueprints)
│   ├── main.py          # Main pages and product catalog
│   ├── auth.py          # Authentication routes
│   ├── cart.py          # Shopping cart functionality
│   └── admin.py         # Admin dashboard routes
├── forms/               # WTForms for validation
│   ├── auth_forms.py    # Login, register, profile forms
│   └── product_forms.py # Product management forms
├── templates/           # Jinja2 HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Homepage
│   ├── products.html    # Product listing
│   ├── product_detail.html # Individual product page
│   ├── auth/           # Authentication templates
│   ├── cart/           # Shopping cart templates
│   └── admin/          # Admin dashboard templates
└── static/             # Static assets
    ├── css/style.css   # Custom CSS with modern design
    ├── js/main.js      # JavaScript functionality
    └── images/         # Product images and assets
```

## Key Features Explained

### User Management
- Secure registration and login system
- Profile management with order history
- Admin role for management access
- Password strength validation

### Product Management
- Complete CRUD operations for products
- Category-based organization
- Stock quantity tracking
- Image support with fallback placeholders
- Size and color variants

### Shopping Experience
- Session-based shopping cart
- Real-time quantity updates
- Checkout with shipping information
- Order confirmation and tracking

### Admin Dashboard
- Overview statistics and metrics
- Product inventory management
- Order status management
- User account oversight
- Low stock alerts

## Database Schema

### Users Table
- Authentication and profile information
- Admin role management
- Order relationship

### Products Table
- Product details and inventory
- Category and variant management
- Stock tracking

### Orders & OrderItems Tables
- Complete order lifecycle
- Item-level details with pricing
- Status tracking system

## Security Features

- Password hashing with Werkzeug
- CSRF protection with Flask-WTF
- Session management with Flask-Login
- Input validation and sanitization
- Admin-only route protection

## Customization

### Adding New Product Categories
1. Update the category choices in `forms/product_forms.py`
2. Add category handling in templates
3. Update navigation if needed

### Styling Modifications
- Edit `static/css/style.css` for visual changes
- Modify templates for layout changes
- Update JavaScript in `static/js/main.js` for interactions

### Database Configuration
- Update `config.py` for PostgreSQL or other databases
- Run Flask-Migrate for schema changes
- Update connection strings as needed

## Production Deployment

### Environment Variables
```bash
export SECRET_KEY="your-secret-key-here"
export DATABASE_URL="your-database-url"
export FLASK_ENV="production"
```

### Database Migration
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## API Endpoints

### Public Routes
- `GET /` - Homepage
- `GET /products` - Product listing with filters
- `GET /product/<id>` - Product details
- `GET /about` - About page
- `GET /contact` - Contact page

### Authentication Routes
- `POST /auth/login` - User login
- `POST /auth/register` - User registration
- `GET /auth/logout` - User logout
- `GET /auth/profile` - User profile
- `GET /auth/orders` - User order history

### Cart Routes (Authenticated)
- `POST /cart/add` - Add item to cart
- `GET /cart/view` - View cart contents
- `POST /cart/update` - Update cart quantities
- `POST /cart/checkout` - Process checkout

### Admin Routes (Admin Only)
- `GET /admin/dashboard` - Admin overview
- `GET /admin/products` - Product management
- `POST /admin/products/add` - Add new product
- `GET /admin/orders` - Order management
- `GET /admin/users` - User management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Email: info@unicornbrand.com
- Documentation: Check the code comments and this README
- Issues: Create an issue in the repository

---

<<<<<<< HEAD
**UNICORN BRAND** - Step Into Excellence 👟✨
=======
**UNICORN BRAND** - Step Into Excellence 👟✨
>>>>>>> 768236fb01da289b1159d2e59cef09923f6b8059
