# blueprints/files.py
from flask import Blueprint, request, redirect, url_for
from flask_login import login_required, current_user
from services.database_service import add_chat_message
import os

files_bp = Blueprint('files', __name__, url_prefix='/files')

@files_bp.route('/upload', methods=['POST'])
@login_required
def upload_file():
    file = request.files['file']
    user_id = current_user.id
    filename = os.path.join('uploads', file.filename)
    file.save(filename)
    add_chat_message(user_id, f"File uploaded: {filename}")
    return redirect(url_for('chat.index'))
