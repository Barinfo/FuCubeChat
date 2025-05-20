import os
import shutil
from datetime import datetime

def backup_database(path):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_path = f"{path}_{timestamp}.bak"
    shutil.copyfile(path, backup_path)
    print(f"Database backed up to {backup_path}")

# 根据实际数据库文件位置调用
# backup_database('path_to_your_database.db')
