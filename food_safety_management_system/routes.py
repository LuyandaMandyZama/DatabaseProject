from flask import Blueprint, request, jsonify
from flask import redirect, url_for
from flask import render_template
from app import db, FoodItem
from .forms import FoodItemForm, UserForm

from flask import Flask
app = Flask(__name__)
from app import models
from .models import User

users_blueprint = Blueprint('users', __name__)

#create
@users_blueprint.route('/users', methods=['POST'])
def create_user():
    pass

#read
@users_blueprint.route('/users', methods=['GET'])
def get_users():
    pass

#update
@users_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_users(user_id):
    pass

#delete
@users_blueprint.route('/users/<intt:user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass

from app import app



@app.route('/add_food_item', methods=['GET', 'POST'])
def add_food_item():
    form = FoodItemForm()
    if form.validate_on_submit():
        
        food_item = FoodItem(
            name=form.name.data,
            description=form.description.data,
            category=form.category.data, 
            expiration_date=form.expiration_date.data, 
        )
        
        db.session.add(food_item)
        db.session.commit()
        return redirect(url_for('list_food_items'))
    return render_template('food_item_form.html', form=form)    


@app.route('/')
def list_food_items():
    food_items = FoodItem.query.all()
    return render_template('food_item_list.html', food_items=food_items)

@app.route('/edit_food_item/<int:id>', methods=['GET', 'POST'])
def edit_food_item(id):
     food_item = FoodItem.query.get_or_404(id)
     form = FoodItemForm(obj=food_item)
     if form.validate_on_submit():
         food_item.name =form.name.data
         food_item.description = form.description.data
         food_item.category = form.category.data
         food_item.expiration_date = form.expiration_date.data
         db.session.commit()
         return redirect(url_for('list_food_items')) 
     return render_template('food_item_form.html', form=form)
 
@app.route('/delete_food_item/<int:id>')
def delete_food_item(id):
     food_item = food_item.query.get_or_404(id)
     db.session.delete(food_item)
     db.session.commit()
     return redirect(url_for('list_food_items'))
 
from .forms import RegistrationForm, LoginForm
from .auth import login, logout 

@app.route('/register', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if form.validate_on_submit():
        if login(form.email.data, form.password.data):
         return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_route():
    logout()
    return redirect(url_for('login'))

from flask_login import login_required 


@app.route('/home')
@login_required
def home():
    return render_template('home.html')