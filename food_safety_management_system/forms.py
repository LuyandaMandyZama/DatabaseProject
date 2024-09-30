from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, NumberRange, InputRequired, Email, Length, EqualTo
from .models import User

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
    
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=2, max=101)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already in use')
        
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=8, max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)]) 
    submit = SubmitField('Login') 
    
class InspectionForm(FlaskForm):
    food_item = StringField('Food Item', validators=[DataRequired()])
    inspection_date = DateField('Inspection Date', validators=[DataRequired()])
    results = TextAreaField('Results', validators=[DataRequired()])
    submit = SubmitField('Save Change')               