# database/models.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128))
    regtime = Column(DateTime, default=datetime.utcnow)

    chats = relationship('Chat', backref='user', lazy=True)

class Chat(db.Model):
    __tablename__ = 'chats'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Emoji(db.Model):
    __tablename__ = 'emojis'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    path = Column(String(255), nullable=False)
    is_approved = Column(Integer, default=0)  # 0: 未审核, 1: 已审核

    user = relationship('User ', backref='emojis', lazy=True)
