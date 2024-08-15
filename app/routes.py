from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import login_user, logout_user, is_logged_in, get_current_user

main = Blueprint('main', __name__)

# Dummy data for demonstration purposes
USERS = {
    "user1": "password1",
    "user2": "password2"
}

@main.route('/')
def home():
    if is_logged_in():
        return f"Welcome, {get_current_user()}! <a href='/logout'>Logout</a>"
    return "You are not logged in. <a href='/login'>Login</a>"

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if USERS.get(username) == password:
            login_user(username)
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid credentials', 'danger')
    
    return render_template('login.html')

@main.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home'))
