from app import db, login_manager
from flask_login import UserMixin
from .models import User
from flask_login import LoginManager, login_user, logout_user
from app import app

class Auth:
    def __init__(self):
        self.login_manager = LoginManager()
        self.login_manager.init_app(app)
        self.login_manager.user_loader(self.load_user)
        

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def authenticate_user(email, password):
    user= User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None

def login(email,password):
    user = authenticate_user(email, password)
    if user:
         login_user(user)
         return True
    return False
 
def logout():
    logout_user()
    return True

auth = Auth()