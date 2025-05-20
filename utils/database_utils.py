# utils/database_utils.py
from database import db

def escape_string(value):
    return db.session.execute("SELECT :value", {'value': value}).scalar()  # 防止 SQL 注入

def sync_database():
    # 数据库同步逻辑
    db.create_all()
