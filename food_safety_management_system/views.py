from flask import render_template, request, redirect, url_for
from app import app
from .forms import FoodItemForm 
from .models import FoodItem
from .extensions import db 

@app.route('/') 
def index(): 
    food_items = FoodItem.query.all()
    return render_template('food_item_list.html', food_items=food_items)

@app.route('/add_food_item', methods=['GET', 'POST'])
def add_food_item():
    form = FoodItemForm()
    if form.validate_on_submit():
        food_item = FoodItem( 
                name=form.name.data,
                description=form.description.data,
                category=form.category.data,
                expiration_date=form.expiration_date.data 
                )
        db.session.add(food_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('food_item_form.html', form=form)

@app.route('/delete_food_item/<int:id>')
def delete_food_item(id):
    food_item = FoodItem.query.get_or_404(id)
    db.session.delete(food_item)
    db.session.commit()
    return redirect(url_for('index'))