from app import db 
class FoodItem(db.model): 
    id= db.Column(db.Integer, primary_key=True) 
    name= db.Column(db.String(100), nullable=False)
    description= db.Column(db.Text)
    category = db.Column(db.String(50))
    expiration_date = db.Column(db.Date)
    
    
def __repr__(self):
    return f'<FoodItem {self.name}>'    
    