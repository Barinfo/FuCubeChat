# services/backup_service.py
import os
import shutil
from datetime import datetime

def backup_database(db_path):
    """备份数据库"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f"{db_path}_backup_{timestamp}.db"
    shutil.copyfile(db_path, backup_path)
    print(f"Database backed up to {backup_path}")

def backup_all_databases():
    """备份所有数据库"""
    from config import Config
    db_paths = [Config.SQLALCHEMY_DATABASE_URI]
    for db_path in db_paths:
        backup_database(db_path)
