from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.declarative import DeclarativeBase
from flask_login import LoginManager
from flask_migrate import Migrate
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:LuyandaZama14@localhost/foodsafetysystem"

db = SQLAlchemy()
Base = db.Model

migrate = Migrate()
login_manager = LoginManager()
#extensions = {'db': db}

extensions = {
    'db': db,
    'migrate': migrate
}
def init_app(app):
    db.init_app(app)
        