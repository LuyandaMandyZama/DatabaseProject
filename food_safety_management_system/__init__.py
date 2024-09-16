#from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from . import app
db = SQLAlchemy(app)

#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'your_secret_key'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_items.db'


#db = SQLAlchemy(app)
#from app import models, forms, views

