from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired

class FoodItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    category = SelectField('Category', choices=[('meat', 'Meat'), ('dairy' 'Dairy'), ('produce', 'Produce') ])
    expiration_date = DateField('Expiration Date')
    
    submit= SubmitField('Submit')