# services/database_service.py
from database import db
from database.models import User, Chat

def get_user_by_id(user_id):
    """根据用户ID获取用户信息"""
    return User.query.get(user_id)

def get_all_chats():
    """获取所有聊天记录"""
    return Chat.query.all()

def add_chat_message(user_id, message):
    """添加一条新的聊天记录"""
    new_message = Chat(user_id=user_id, message=message)
    db.session.add(new_message)
    db.session.commit()

def update_user_info(user_id, username, email):
    """更新用户信息"""
    user = User.query.get(user_id)
    if user:
        user.username = username
        user.email = email
        db.session.commit()

def delete_user(user_id):
    """删除用户"""
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
