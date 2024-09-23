import secrets

SECRET_KEY = secrets.token_urlsafe(32)

import os 

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:LuyandaZama14@localhost:3306/foodsafetysystem'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False