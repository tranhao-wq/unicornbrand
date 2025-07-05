from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Length
from flask_wtf.file import FileField, FileAllowed

PRODUCT_CATEGORIES = [
    ('sneakers', 'Sneakers'),
    ('boots', 'Boots'),
    ('sandals', 'Sandals'),
    ('formal', 'Formal Shoes'),
    ('sports', 'Sports Shoes'),
    ('casual', 'Casual Shoes')
]

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description')
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.01)])
    category = SelectField('Category', choices=PRODUCT_CATEGORIES, validators=[DataRequired()])
    brand = StringField('Brand', default='UNICORN BRAND')
    image = FileField('Product Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    stock_quantity = IntegerField('Stock Quantity', validators=[DataRequired(), NumberRange(min=0)])
    sizes = StringField('Available Sizes (comma-separated)', 
                       validators=[DataRequired()],
                       render_kw={'placeholder': '6,7,8,9,10,11,12'})
    colors = StringField('Available Colors (comma-separated)', 
                        validators=[DataRequired()],
                        render_kw={'placeholder': 'Black,White,Red,Blue'})
    is_active = BooleanField('Active Product', default=True)
    submit = SubmitField('Save Product')

class SearchForm(FlaskForm):
    query = StringField('Search products...', 
                       render_kw={'placeholder': 'Search by name, brand, or category'})
    category = SelectField('Category', choices=[('', 'All Categories')] + PRODUCT_CATEGORIES)
    min_price = FloatField('Min Price', validators=[NumberRange(min=0)])
    max_price = FloatField('Max Price', validators=[NumberRange(min=0)])
    submit = SubmitField('Search')