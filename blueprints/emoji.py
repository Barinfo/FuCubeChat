# blueprints/emoji.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from utils.emoji_processor import EmojiProcessor

emoji_bp = Blueprint('emoji', __name__, url_prefix='/emoji')

@emoji_bp.route('/')
@login_required
def index():
    # 列出所有表情包
    return render_template('emoji/square.html')

@emoji_bp.route('/upload', methods=['POST'])
@login_required
def upload():
    file = request.files['file']
    processor = EmojiProcessor()
    result = processor.process_upload(file)
    return redirect(url_for('emoji.index'))
