from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import secrets
import pymysql

SECRET_KEY = secrets.token_urlsafe(32)
pymysql.install_as_MySQLdb()
    
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:LuyandaZama14@localhost/foodsafetysystem'
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
    'default' : 'mysql+pymysql://root:LuyandaZama14@localhost/foodsafetysystem'
    }
    SECRET_KEY = SECRET_KEY
    
#app = Flask(__name__)
#app.config.from_object(Config)

#db = SQLAlchemy()
#print(app.config['SQLALCHEMY_DATABASE_URI'])       