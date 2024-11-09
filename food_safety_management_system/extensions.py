from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
Base = db.Model

migrate = Migrate()
login_manager = LoginManager()


extensions = {
    'db': db,
    'migrate': migrate
}

