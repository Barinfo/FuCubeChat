# blueprints/chat.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from services.database_service import get_all_chats, add_chat_message

chat_bp = Blueprint('chat', __name__, url_prefix='/chat')

@chat_bp.route('/')
@login_required
def index():
    chats = get_all_chats()
    return render_template('chat/index.html', chats=chats)

@chat_bp.route('/send_message', methods=['POST'])
@login_required
def send_message():
    message = request.form['message']
    user_id = current_user.id
    add_chat_message(user_id, message)
    return redirect(url_for('chat.index'))
