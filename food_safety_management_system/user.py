from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        
    def check_password(self, provided_password):
        return check_password_hash(self.password, provided_password)
    
    def get_id(self):
        return str(self.id)