from flask import Flask


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
    
      