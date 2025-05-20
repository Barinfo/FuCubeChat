# utils/auth.py
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user

login_manager = LoginManager()

def configure_auth(app):
    login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    from database.models import User
    return User.query.get(int(user_id))

def authenticate_user(username, password):
    from database.models import User
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        login_user(user)
        return True
    return False

def logout():
    logout_user()
