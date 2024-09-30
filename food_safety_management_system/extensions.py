from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = None
migrate = Migrate()
login_manager = LoginManager()
#extensions = {'db': db}

extensions = {
    'db': db,
    'migrate': migrate
}