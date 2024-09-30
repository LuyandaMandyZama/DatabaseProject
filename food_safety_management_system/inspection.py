from .models import Violation
from datetime import date, timedelta

def detect_violations(inspection):
    violations = [ ]
    
    if  inspection.temperature < 39 or inspection.temperature > 140:
        violations.append(Violation(
            inspection_id='inspection_id',
            description='Temperature is OUT OF RANGE',
            severity = 'High',
            
         storage_location=inspection.storage_location, inspection=inspection   
        ))
        
        if inspection.expiration_date < date.today():
            violations.append(Violation(
                inspection_id='inspection_id',
                description='Expired Product',
                severity='High',
                
            storage_location=inspection.storage_location, inspection=inspection    
            ))
            
        if inspection.storage_capacity < inspection.product_quantity:
            violations.append(Violation(
                inspection_id='inspection_id',
                description='inadequate storage space',
                severity='Medium',
                
            storage_location=inspection.storage_location, inspection=inspection    
            ))    
            
            return violations