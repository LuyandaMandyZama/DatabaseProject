import os
import secrets
import pymysql
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from .config import Config
from food_safety_management_system.extensions import extensions, db, migrate
from .models import FoodItem, User, Inspection, Violation, FoodItemSchema
from datetime import datetime

#pymysql.install_as_MySQLdb()  
app = Flask(__name__)
app.config.from_object(Config)

#SECRET_KEY = secrets.token_urlsafe(32)
#pymysql.install_as_MySQLdb()
    
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:LuyandaZama14@localhost/foodsafetysystem'
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
    'default' : 'mysql+pymysql://root:LuyandaZama14@localhost/foodsafetysystem'
    }
    SECRET_KEY = secrets.token_urlsafe(32)
    
app.config.from_object(Config)
     
#app.config.from_pyfile('config.py')
#app.config.from_object('Config')
#print("App Config: ", app.config )
#print("SQLALCHEMY_DATABASE_URI:", app.config['SQLALCHEMY_DATABASE_URI'])
#print("Setting SQLAlchemy_DATABASE_URI")
#SECRET_KEY = app.config['SECRET_KEY']
#def init_app(app):
app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('SQLALCHEMY_DATABASE_URI','mysql://root:LuyandaZama14@localhost/foodsafetysystem')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#init_app(app)
#db = SQLAlchemy(app)
def init_app(app):
   db.init_app(app)

#migrate = Migrate()
migrate = Migrate(app, db, directory='C:\DatabaseProject\\migrations')

#print("App Config: ", app.config)
#print("SQLAlchemy_DATABASE_URI: ", app.config['SQLALCHEMY_DATABASE_URI'])
#for name, ext in extensions.items():
 #  if hasattr(ext, 'init_app'):
  #   exit.init_app(app)
#db.init_app(app)
#with app.app_context():
 #  migrate.init_app(app, db)

#with app.app_context():
 #  db.create_all()

    
@app.before_request 
def before_request_func():
   pass
   
@app.route('/users', methods=['POST'])
def create_user():
   data = request.get_json()
   user = User(**data)
   db.session.add(user)
   db.session.commit()
   return jsonify(user.to_dict()), 201

@app.route('/users', methods=['GET'])
def get_users():
   users = User.query.all()
   return jsonify([user.to_dict() for user in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
   user = User.query.get_or_404(user_id)
   return jsonify(user.torequest_dict())

from sqlalchemy import text

@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
   data = request.get_json()
   name = data.get('name')
   email = data.get('email')
   query = text("SELECT * FROM user WHERE id = :id")
   result = db.session.execute(query, {"id": user_id})
   user = result.fetchone()
   
   if user is None:
      return jsonify({"error":"User Not Found"}), 404
   
   update_query = text("UPDATE user SET name = :name, email = :email WHERE id = :id")
   db.session.execute(update_query, {"name": name, "email": email, "id":user_id})
   db.session.commit()
   return jsonify({"message" : "User Updated Successfullly"}), 200
   
 #  data = request.get_json()
  # user = User.query.get(user_id)
   #if not user:
    #  return jsonify({ 'message' : 'User Not Found' }), 404
   
   #data = request.get_json() 
   #if 'email' in data: 
    #  user.email = data['email']
   #db.session.commit()
   
   #return jsonify(user.to_dict()), 200

   #user = User.query.filter_by(email=email).first()
   #if user:
    #  data = request.get_json()
     # user.email = data.get('email')  
      #user.name = data.get('name') 
      #db.session.commit() 
      #return jsonify(user.to_dict()) 
   #return jsonify({'message' : 'User Not Found'}), 

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
   query = text("SELECT * FROM user WHERE id = :id") 
   result = db.session.execute(query, {"id":user_id})
   user = result.fetchone()
   if user is None: 
      return jsonify({"error": "User Not Found"}), 404
   delete_query = text("DELETE FROM user WHERE id = :id")
   db.session.execute(delete_query, {"id":user_id})
   db.session.commit()
   return jsonify({"message":"User has been DELETED"}), 200
      
   

 
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

@app.route('/update-item/<string:item_name>', methods=['PUT'])
def update_item(item_name):
   food_item = FoodItem.query.filter_by(name=item_name).first_or_404( )
   
   
   data = request.get_json()
   food_item.name = data.get('name', food_item.name)
   food_item.description = data.get('description', food_item.description)
   food_item.category = data.get('category', food_item.category)
   food_item.expiration_date = datetime.strptime(data.get('expiration_date', food_item.expiration_date.strftime('%Y-%m-%d')), '%Y-%m-%d')
   
   
   db.session.commit()
   
   return jsonify({'message': 'Item Updated Successfully' }), 200

@app.route('/delete-item/<string:item_name>', methods=['DELETE'])
def delete_item(item_name):
   food_item = FoodItem.query.filter_by(name=item_name).first_or_404()
   db.session.delete(food_item)
   db.session.commit()
   
   return jsonify({'message': 'Item Deleted Successfully'}), 200

@app.route('/get-item/<string:item_name>', methods=['GET'])
def get_item(item_name):
   food_item = FoodItem.query.filter_by(name=item_name).first_or_404()
   return jsonify({
      'id' : food_item.id, 
      'name' : food_item.name,
      'description' : food_item.description,
      'category' : food_item.category,
      'expiration_date' : food_item.expiration_date.strftime('%Y-%m-%d') if food_item.expiration_date else 'No Expiration Date'
   }), 200
   
@app.route('/inspections', methods=['GET'])  
def get_all_inspections(): 
   inspections = Inspection.query.all() 
   return jsonify([inspection.to_dict() for inspection in inspections]) 
 
@app.route('/inspections', methods=['POST'])
def create_inspection():
   data = request.get_json() 
   inspection = Inspection(
      food_item_id=data['food_item_id'],
      inspection_date=data['inspection_date'],
      entity_type=data['entity_type'],
      entity_id=data['entity_id'],
      temperature=data['temperature'],
      results=data['results']
   )
   db.session.add(inspection)
   db.session.commit()
   #return jsonify({'message':'Inspection Created', 'id':})
   return jsonify(inspection.to_dict()), 201
 
@app.route('/inspections/<id>', methods=['PUT'])
def update_inspection(id):
   try:
      inspection = Inspection.query.get(id)
      if inspection:
        data = request.get_json()
        inspection.food_item_id= data.get('food_item_id')
        inspection.inspection_date= data.get('inspection_date')
        inspection.entity_type=data.get('entity_type')
        inspection.entity_id=data.get('entity_id')
        inspection.temperature=data.get('temperature')
        inspection.results = data.get('results') 
        db.session.commit()
        return jsonify(inspection.to_dict())
      return jsonify({'message': 'Inspection Not Found'}), 404
   except Exception as e:
      print(f"Error: {e}")
      return jsonify({'error':'An error occurred'}), 500
 
@app.route('/inspections/<id>', methods=['DELETE'])
def delete_inspection(id):
   inspection = Inspection.query.get(id)
   if inspection:
      db.session.delete(inspection)
      db.session.commit()
      return jsonify({'message': 'Inspection Deleted'})
   return jsonify({'message': 'Inspection Not Found'}), 404
 
@app.route('/violations', methods=['GET'])
def get_all_violations():  
   violations = Violation.query.all()
   return jsonify([violation.to_dict() for violation in violations])

@app.route('/violations', methods=['POST'])
def create_violation():
   data = request.get_json()
   violation = Violation(
      inspection_id=data['inspection_id'],
      description=data['description'],
      severity=data['severity'],
      storage_location=data['storage_location']
   ) 
   db.session.add(violation)
   db.session.commit()
   return jsonify(violation.to_dict()), 201

@app.route('/violations/<id>', methods=['PUT'])
def update_violation(id):
   violation = Violation.query.get(id)
   if violation:
      data = request.get_json()
      violation.description =data.get('description')
      violation.severity = data.get('severity')
      violation.storage_location = data.get('storage_location')
      db.session.commit()
      return jsonify(violation.to_dict())
   return jsonify({'message':'Violation Not Found'}), 404

@app.route('/violations/<id>', methods=['DELETE'])
def delete_violation(id):
   violation = Violation.query.get(id)
   if violation:
      db.session.delete(violation)
      db.session.commit()
      return jsonify({'message': 'Violation Deleted'})

from flask import Flask, render_template, redirect, url_for, flash, Blueprint 
from flask_login import LoginManager,  login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from .forms import RegistrationForm

from .user import User
auth_blueprint= Blueprint('auth',__name__)

from .config import SECRET_KEY 
app.config['SECRET_KEY']

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  

login_manager.blueprint_name = 'auth_blueprint'

app.register_blueprint(auth_blueprint, name='auth')

from flask_bcrypt import bcrypt

@app.route('/register', methods=['GET', 'POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
      user = User( 
      email = form.email.data,
      password_hash = hashed_password )
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      db.session.add(user) 
      db.session.commit()
      return redirect(url_for('auth.login'))
   return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.methods == 'POST':
      email = request.form['email']
      password = request.form['password'] 
      user = User.query.filter_by(email=email).first()
      if user and user.check_password(password):
         login_user(user)
         return redirect(url_for('dashboard'))
      flash('Invalid email or password', 'danger')
      return render_template('login.html')   

@app.route('/dashboard', methods=['GET'])
def dashboard_main():
   return render_template('dashboard.html')

@app.route('/logout')
@login_required
def dashboard():
   return render_template('dashboard.html', name=current_user.email)

from .config import Config 
from .routes import inspection_bp 
from .inspection import *
app.register_blueprint(inspection_bp)
@app.route('/inspection_report')
def inspection_report():
   cursor = cursor()
   cursor.execute("SELECT * FROM inspection")
   data = cursor.fetchall()
   return render_template('inspection_report.html', data=data)

@app.route('/violation_summary')
def violation_summary():
   cursor=cursor()
   cursor.execute("SELECT * FROM violation")
   data = cursor.fetchall()
   return render_template('vision_summary.html', data=data)

@app.shell_context_processor
def startup(): 
   print("App is now SERVING")
   return{}

@app.route('/favicon.ico')
def favicon():
   return "", 204



if __name__ == '__main__': 
   db.create_all()

app.run(debug=True, use_reloader=True)

