import pytest
from flask import json 
from customers_app import *

def test_api_get_customer():
    response = app.test_client().get('/api/customers/HBW00')
    data = json.loads(response.get_data(as_text=True))
    assert "Hassan Bilal Wehbi" in str(response.data)
    
def test_api_add_customer():
    response = app.test_client().post(
        '/api/customers/add',
        data=json.dumps({ 
            "FullName": "Mahdi Mouayad Zwein",
            "UserName": "mmz45",
            "Password": "12345",
            "Age": "21",
            "Address": "Baghdad",
            "Gender": "Male",
            "MaritalStatus" : "Single"
        }),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['Address'] == "Baghdad"
    
def test_api_delete_customer():
    response = app.test_client().delete('/api/customers/delete/mmz45')
    data = json.loads(response.get_data(as_text=True))  
    assert "User deleted successfully"  in str(response.data)
    
def test_api_get_customers():
    response = app.test_client().get('/api/customers')
    data = json.loads(response.get_data(as_text=True))
    assert data[0]['FullName'] == "Hassan Bilal Wehbi"
    
def test_api_update_customer():
    response = app.test_client().put(
        '/api/customers/update',
        data=json.dumps({ 
            "FullName": "Hassan Bilal Wehbi",
            "UserName": "HBW00",
            "Password": "23141817",
            "Age": "18",
            "Address": "Beirut",
            "Gender": "Male",
            "MaritalStatus" : "Multi Single"
        }),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert data['MaritalStatus'] == "Multi Single"