import secrets

SECRET_KEY = secrets.token_urlsafe(32)

import os 
import pymysql

pymysql.install_as_MySQLdb()

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:LuyandaZama14@localhost:3306/foodsafetysystem'
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 30
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False