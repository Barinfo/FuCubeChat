# blueprints/admin.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from services.database_service import get_all_chats, update_user_info, delete_user

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
@login_required
def index():
    chats = get_all_chats()
    return render_template('admin/index.html', chats=chats)

@admin_bp.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def update_user(user_id):
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        update_user_info(user_id, username, email)
        return redirect(url_for('admin.index'))
    user = get_user_by_id(user_id)
    return render_template('admin/update_user.html', user=user)

@admin_bp.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user_route(user_id):
    delete_user(user_id)
    return redirect(url_for('admin.index'))
