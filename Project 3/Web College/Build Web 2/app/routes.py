from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, session
from .models import User
from . import db, bcrypt

auth = Blueprint('auth', __name__)

# Login Route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            flash('Username and password are required.')
            return redirect(url_for('auth.login'))

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('auth.dashboard'))

        flash('Invalid credentials, please try again')
        return redirect(url_for('auth.login'))
    
    # Display login form
    return render_template('login.html')

# Register Route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            flash('Username and password are required.')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('auth.register'))

        # Hash the password before storing
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.')
        return redirect(url_for('auth.login'))
    
    # Display registration page
    return render_template('register.html')

# Logout route
@auth.route('/logout')
def logout():
    session.pop('user_id', None)  # Clear session
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))

# Dashboard Route (protected page)
@auth.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page.')
        return redirect(url_for('auth.login'))
    
    return render_template('dashboard.html')