# blueprints/auth.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
from services.database_service import get_user_by_id
from utils.auth import authenticate_user

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            return redirect(url_for('chat.index'))
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
