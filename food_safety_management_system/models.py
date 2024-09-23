#from .models import db 
#from food_safety_management_system import db
from food_safety_management_system.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Text, Date 
from sqlalchemy.ext.declarative import   declarative_base 
Base = declarative_base()

db = SQLAlchemy()

class User(db.Model, Base): 
    __tablename__ = 'User'
    
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User{self.name}, {self.email}>"

class FoodItem(db.Model, Base): 
    __tablename__ = 'food_item'
    
    id= db.Column(db.Integer, primary_key=True, autoincrement=True) 
    name= db.Column(db.String(100), nullable=False)
    description= db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    
   
    
def __repr__(self):
    return f"<FoodItem {self.name}, {self.category}>"   

class Inspection(db.Model, Base):
    __tablename__ = 'inspection'
    
    id= db.Column(db.Integer, primary_key=True)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_item.id'))
    inspection_date = db.Column(db.DateTime)
result=db.Column(db.String(50))

food_item = db.relationship('FoodItem', backref=db.backref('inspections', lazy=True))

def __repr__(self):
    return f"<Inspection {self.inspection.date} {self.result}>"


class Violation(db.Model):
    __tablename__ = 'violation'
    
    id = db.Column(db.Integer, primary_key=True)
    inspection_id = db.Column(db.Integer, db.ForeignKey('inspection.id'))
    description = db.Column(db.Text)
    severity = db.Column(db.String(50))
    
    inspection = db.relationship('Inspection', backref=db.backref('violations', lazy=True))
    
def __repr__(self):
    return f"<Violation {self.description}, {self.severity}>" 


#
#from .app import app, db 
#with app.app_context():
    #db.create_all