from food_safety_management_system.extensions import db, login_manager
from flask_login import UserMixin, login_user, logout_user, login_required 
from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm, InspectionForm
from .models import User, db, Inspection
from flask_login import LoginManager, login_user, logout_user
from food_safety_management_system.app import app
from werkzeug.security import generate_password_hash
#from app.auth import auth
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, DateField, TextAreaField, SubmitField

auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder='template')

class Auth:
    
 login_manager = LoginManager(auth_blueprint)
 login_manager.blueprint_name= 'auth_blueprint'        

@staticmethod
 
  
def __init__(self):
    self.login_manager = LoginManager()
    self.login_manager.init_app(app)
    self.login_manager.user_loader(self.load_user)

def register(email, password): 
    user = User(email=email)
    user.set_password(password)

def authenticate_user(self, email, password):
    user= User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None

def login(self,email,password):
    user = authenticate_user(email, password)
    if user:
         login_user(user)
         return True
    return False
 
def logout(self):
    logout_user()
    return True


from flask_bcrypt import Bcrypt 

bcrypt = Bcrypt(app)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            name = form.name.data,
            email = form.email.data,
            password_hash = hashed_password
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_blueprint.route('/login', methods=['GET', 'POST']) 
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard_main'))
        else:
            flash('Invalid Credentials')
    return render_template('login.html', form=form)

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_blueprint.login'))

@auth_blueprint.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html')

@auth_blueprint.route('/inspection-history', methods=['GET'])
@login_required
def inspection_history():
    inspections = Inspection.query.all()
    return render_template('inspection_history.html', inspections=inspections)

@auth_blueprint.route('/view-inspection', methods=['GET']) 
@login_required
def view_inspection(inspection_id): 
    inspection = Inspection.query.get(inspection_id)
    return render_template('view_inspection.html', inspection=inspection)

@auth_blueprint.route('/edit-inspection/<int:inspection_id>', methods=['GET', 'POST'])
@login_required 
def edit_inspection(inspection_id):
    inspection = Inspection.query.get(inspection_id)
    form = InspectionForm(obj=inspection)
    if form.validate_on_submit():
      form.populate_obj(inspection)
      db.session.commit()
      return redirect(url_for('auth.inspection_history'))
    
    return render_template('edit_inspection.html', inspection=inspection, form=form)



@auth_blueprint.route('/add-inspection', methods=['GET', 'POST'])
@login_required
def add_inspection(inspection_id):
    form = InspectionForm()
    if form.validate_on_submit():
        inspection = Inspection(**form.data)
        db.session.add(inspection)
        db.session.commit()
        return redirect(url_for('auth.inspection_history'))
    return render_template('add_inspection.html', form=form)   

@auth_blueprint.route('/submit-inspection/<int:inspection_id>', methods=['POST'])
@login_required
def submit_inspection(inspection_id):
    inspection = Inspection.query.get(inspection_id) 
    if not inspection:
        flash("Inspection Not Found", "error")
        return redirect(url_for('auth.inspection_history'))
        
        inspection.status = "submitted"
        db.session.commit()
        
        notification = Notification( 
                                    message=f"Inspection {( inspection_id)} submitted by {current_user.name}", user_id=user.id 
                                    )
        db.session.add(notification)
        db.session.commit()
        
        flash("Inspection Submited!", "success")
        return redirect(url_for('auth.inspection-history'))
           
@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))