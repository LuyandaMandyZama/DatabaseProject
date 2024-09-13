from app import db 
class FoodItem(db.model): id= db.Column(db.Integer, primary_key=True)  name= db.Column(db.String(100), nullable=False)