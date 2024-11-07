from flask import Blueprint, jsonify, request
from .models import Violation, Inspection
from datetime import date, timedelta

inspection_bp = Blueprint('unique_inspection_bp', __name__)

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

@inspection_bp.route('/detect_violations', methods=['POST'])
def detect_violations_endpoint():
    inspection_data = request.get_json()
    inspection = Inspection(**inspection_data)
    violations = detect_violations(inspection)
    return jsonify([violation.to_dict() for violation in violations])