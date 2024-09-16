import os

from flask import current_app
app= current_app 
with app.app_context():
#app = Flask(__name__)
 app.config.from_pyfile('config.py')

SECRET_KEY = app.config['SECRET_KEY']
#@app.route('/')
#def hello_world():
 #   return 'Hello World'

if __name__ == '__main__': 
 app.run(debug=True, use_reloader=True)
#app,static_folder = 'static'

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:LuyandaZama14@localhost/foodsafetysystemdb'

db = SQLAlchemy(app)

from flask_migrate import Migrate 

migrate = Migrate(app, db)