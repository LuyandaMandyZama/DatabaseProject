import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
#from food_safety_management_system.database import db
from food_safety_management_system.extensions import extensions, db, migrate
from food_safety_management_system.models import FoodItem, User, Inspection, Violation, db
from datetime import datetime
  
app = Flask(__name__)
app.config.from_pyfile('config.py')

SECRET_KEY = app.config['SECRET_KEY']

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:LuyandaZama14@localhost/foodsafetysystem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
migrate = Migrate(app, db)

#for name, ext in extensions.items():
 #  if hasattr(ext, 'init_app'):
  #   exit.init_app(app)
db.init_app(app) 
migrate.init_app(app, db)

with app.app_context():
   db.create_all()

@app.before_request 
def before_request_func():
   pass
   
 
#@app.route('/')
#def hello_world():
 #   return 'Hello World' 
 
@app.route('/add-item/<string:name>/<string:description>/<string:category>/<string:expiration_date>')
def add_item(name, description, category, expiration_date):
   expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d')
   new_item = FoodItem(
      name=name,
      description = description,
      category = category,
      expiration_date=expiration_date
      ) 
   db.session.add(new_item)
   db.session.commit()
   return f"Added {name} to the database with expiration date {expiration_date.date()}."


@app.route('/get-items', methods=['GET'])
def get_items():
   items = FoodItem.query.all()
   return [{'id': item.id,
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'expiration_date': item.expiration_date.strftime('%Y-%m-%d')} for item in items]
   

@app.shell_context_processor
def startup(): 
   print("App is now SERVING")
   return{}


if __name__ == '__main__': 
   db.create_all()

 #for extension in extensions.values():
  #  extension.init_app(app)    
   # with app.app__all():
app.run(debug=True, use_reloader=True)
#app,static_folder = 'static'
