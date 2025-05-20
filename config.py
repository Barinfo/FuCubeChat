import os
from dotenv import load_dotenv
from flask import current_app

# 加载环境变量
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///fucubechat.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.environ.get("FLASK_DEBUG", "True").lower() in ['true', '1', 't']

    # 初始邮件配置，从环境变量加载
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.example.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', '1', 't']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    @staticmethod
    def init_app(app):
        # 在这里可以执行与当前配置相关的初始化工作
        # 例如，动态更新邮件配置
        app.config['MAIL_SERVER'] = current_app.config.get('MAIL_SERVER', Config.MAIL_SERVER)
        app.config['MAIL_PORT'] = current_app.config.get('MAIL_PORT', Config.MAIL_PORT)
        app.config['MAIL_USE_TLS'] = current_app.config.get('MAIL_USE_TLS', Config.MAIL_USE_TLS)
        app.config['MAIL_USERNAME'] = current_app.config.get('MAIL_USERNAME', Config.MAIL_USERNAME)
        app.config['MAIL_PASSWORD'] = current_app.config.get('MAIL_PASSWORD', Config.MAIL_PASSWORD)

# 开发和生产配置可以从基础配置继承
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL", "sqlite:///dev_fucubechat.db")

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

# 应用配置初始化
# 在应用工厂函数中根据当前环境选择配置类
# 例如:
# app.config.from_object('config.DevelopmentConfig')  # 开发环境
# app.config.from_object('config.ProductionConfig')   # 生产环境
