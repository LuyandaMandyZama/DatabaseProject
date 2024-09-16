from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class FoodItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    category = SelectField('Category', choices=[('meat', 'Meat'), ('dairy' 'Dairy'), ('produce', 'Produce') ])
    expiration_date = DateField('Expiration Date')
    
    submit= SubmitField('Submit')
    
    
class UserForm(FlaskForm):
    name= StringField('Name', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired()])
    submit= SubmitField('Submit')