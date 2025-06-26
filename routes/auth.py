from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from models.user import User
from forms.auth_forms import LoginForm, RegistrationForm, ProfileForm
from database import db
import os
from werkzeug.utils import secure_filename

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            flash(f'Welcome back, {user.get_full_name()}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        flash('Invalid email or password', 'error')
    
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.phone = form.phone.data
        current_user.address = form.address.data
        # Xử lý upload avatar
        if form.avatar.data:
            filename = secure_filename(form.avatar.data.filename)
            avatar_folder = os.path.join('static', 'assets', 'images', 'avatars')
            os.makedirs(avatar_folder, exist_ok=True)
            avatar_path = os.path.join(avatar_folder, filename)
            form.avatar.data.save(avatar_path)
            current_user.avatar = filename
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('auth.profile'))
    
    # Pre-populate form with current user data
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.phone.data = current_user.phone
    form.address.data = current_user.address
    
    return render_template('auth/profile.html', form=form)

@auth_bp.route('/orders')
@login_required
def orders():
    from models.order import Order
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template('auth/orders.html', orders=orders)