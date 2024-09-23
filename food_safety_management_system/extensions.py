from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

db = None
migrate = Migrate()

#extensions = {'db': db}

extensions = {
    'db': db,
    'migrate': migrate
}