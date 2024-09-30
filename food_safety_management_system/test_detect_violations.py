from .models import Inspection, Violation, db
from .inspection import detect_violations
from datetime import date, timedelta
from flask_testing import TestCase
from .app import app,db

from .routes import inspection_bp
import unittest
from unittest.mock import Mock, patch

class TestViolationDetection(unittest.TestCase):
    
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app
    
    def setUp(self):
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
    def test_create_inspection(self):
        inspection = Inspection(
            food_item_id=1,
            inspection_date=date.today(),
            result="Pass",
            temperature=37.8
        )        
        db.session.add(inspection)
        db.session.commit()
        self.assertEqual(Inspection.query.count() , 1)
        
    def test_inspection_attributes(self):
        inspection = Inspection(
            food_item_id = 1,
            inspection_date = date.today(),
            result='Pass', 
            temperature=37.8
        )
        
        db.session.add(inspection)
        db.session.commit()
        stored_inspection_count = Inspection.query.count()
        self.assertEqual(stored_inspection_count, 1)
        stored_inspection = Inspection.query.first()
    
        self.assertEqual(stored_inspection.food_item_id, 1)    
        self.assertEqual(stored_inspection.inspection_date, date.today())
        self.assertEqual(stored_inspection.result,"Pass")
        self.assertEqual(stored_inspection.temperature, 37.8)
     
    
     
    def test_temperature_violation(self): 
        inspection = Inspection(
            food_item_id=1,
            inspection_date=date.today(),
            results="Pass",
            temperature=40.0
        ) 
        db.session.add(inspection)
        db.session.commit()
        violations = detect_violations(inspection) 
        self.assertEqual(len(violations), 1)
        
    def test_inspection_date_violation(self):
        inspection = Inspection(
            food_item_id=1,
            
            inspection_date=date.today()-timedelta(days=30),
            results="Pass",
            temperature=37.8
        )
        db.session.add(inspection)
        db.session.commit()
        violations = detect_violations(inspection)
        self.assertEqual(len(violations), 1)
             
    if __name__ == '__main__':
        unittest.main()       
        