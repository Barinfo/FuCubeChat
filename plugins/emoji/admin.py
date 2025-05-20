# plugins/emoji/admin.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from services.database_service import get_all_emojis, approve_emoji, reject_emoji

emoji_admin_bp = Blueprint('emoji_admin', __name__, url_prefix='/admin/emoji')

@emoji_admin_bp.route('/')
@login_required
def index():
    emojis = get_all_emojis()  # 获取待审核的表情包
    return render_template('admin/emoji.html', emojis=emojis)

@emoji_admin_bp.route('/approve/<int:emoji_id>', methods=['POST'])
@login_required
def approve(emoji_id):
    approve_emoji(emoji_id)  # 审核通过
    return redirect(url_for('emoji_admin.index'))

@emoji_admin_bp.route('/reject/<int:emoji_id>', methods=['POST'])
@login_required
def reject(emoji_id):
    reject_emoji(emoji_id)  # 拒绝审核
    return redirect(url_for('emoji_admin.index'))
