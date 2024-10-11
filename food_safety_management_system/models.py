from flask import Flask
#from  food_safety_management_system import db 
from .database import db
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
#from .app import db 
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Text, Date 
from sqlalchemy.ext.declarative import   declarative_base 
Base = declarative_base()

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:LuyandaZama14@localhost/foodsafetysystem'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



#db = SQLAlchemy(app)
ma = Marshmallow()

class User(db.Model, Base, UserMixin): 
    __tablename__ = 'User'
    
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), unique=True, nullable=False)
    password_hash= db.Column(db.String(120), nullable=False)  
    
    def to_dict(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'email' : self.email,
            'password_hash' : self.password_hash,
        }
        
    def __init__(self, name, email, password): 
        self.name = name
        self.email = email
        self.password = password
    
    
    @classmethod 
    def delete_by_id(cls, user_id):
        user = cls.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit() 
            return True
        return False
        
    @property
    def is_active(self):
        return True
    
from werkzeug.security import generate_password_hash, check_password_hash
    
def set_password(self, password): 
        self.password_hash = generate_password_hash(password)
        
def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
def __repr__(self):
    return f"<User {self.email}>"

class Auth:
    def register(self, email, password):
        if User.query.filter_by(email=email).first():
            return "User Already Exists" 
           
        new_user = User(email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return "User registered successfully!"
  


def login(self, username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_passsword(password):
        return "Invalid Login Details"
    return "Login Successful!"

def get_user(self, username):
    return User.query.filter_by(username=username).first()

def to_dict(self): 
        return {
            'id' : self.id, 
            'name' : self.name,
            'email' : self.email,
            'password_hash' : self.password_hash
        }
def __repr__(self):
        return f"<User{self.name}, {self.email}>"

class FoodItem(db.Model, Base): 
    __tablename__ = 'food_item'
    
    id= db.Column(db.Integer, primary_key=True, autoincrement=True) 
    name= db.Column(db.String(100), nullable=False)
    description= db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    
def to_dict(self):
     return {
         'id': self.id,
         'name': self.name,
         'description': self.description,
         'category': self.category,
         'expiration_date': self.expiration_date.strftime('%Y-%m-%d') if self.expiration_date else None
     }
     
class FoodItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model =  FoodItem 
        
        load_instance = True      
    
def __repr__(self):
    return f"<FoodItem {self.name}, {self.category}>"   

class Inspection(db.Model, Base):
    __tablename__ = 'inspection'
    
    id= db.Column(db.Integer, primary_key=True)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_item.id'))
    inspection_date = db.Column(db.DateTime)
    entity_type = db.Column(db.String(100), nullable=False)
    entity_id = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    results=db.Column(db.String(50), nullable=False)

    food_item = db.relationship('FoodItem', backref=db.backref('inspections', lazy=True))
    
    def __init__(self, food_item_id, inspection_date, entity_type, entity_id, temperature, results):
        self.food_item_id = food_item_id
        self.inspection_date = inspection_date
        self.entity_type = entity_type
        self.temperature = temperature
        self.results = results
        
    def __repr__(self):
        return f"<Inspection {self.id}: {self.entity_type} - {self.results}>" 
     
    def to_dict(self):
        return {
        'id' : self.id,
        'food_item_id' : self.food_item_id,
        'inspection_date': self.inspection_date.isoformat(),
        'entity_type' : self.entity_type,
        'entity_id' : self.entity_id,
        'temperature' : self.temperature,
        'results' : self.results 
    }


class Violation(db.Model):
    __tablename__ = 'violation'  
    __allow_unmapped__ = True
    id = db.Column(db.Integer, primary_key=True)
    inspection_id = db.Column(db.Integer, db.ForeignKey('inspection.id'))
    description = db.Column(db.Text)
    severity = db.Column(db.String(50))
    storage_location = db.Column(db.String(255), nullable=False)
    inspection = db.relationship('Inspection', backref=db.backref('violations', lazy=True))
    
    def to_dict(self):
        return {
            'id' : self.id,
            'inspection_id' : self.inspection_id,
            'description' : self.description,
            'severity' : self.severity,
            'storage_location' : self.storage_location  
        }
def __repr__(self):
    return f"<Violation {self.description}, {self.severity}>" 


