from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

SECRET_KEY = secrets.token_urlsafe(32)

import os 
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:LuyandaZama14@localhost/foodsafetysystem'
db = SQLAlchemy(app)
    
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:LuyandaZama14@localhost/foodsafetysystem'
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
print(app.config['SQLALCHEMY_DATABASE_URI']) 

SQLALCHEMY_BINDS = {
    'default' : 'mysql://root:LuyandaZama14@localhost/foodsafetysystem'
}   