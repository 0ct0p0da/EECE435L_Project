import pytest
from flask import json 
from app2 import *

def test_api_add_item():
    response = app.test_client().post(
        '/api/Inventory/add',
        data=json.dumps({ 
            'itemId' : 3,
            'itemName': "T-shirt",
            'itemCategory': "Clothes",
            'itemPrice': 11.2,
            'itemDescription': "A T-shirt is a type of shirt that has a T shape and no collar" ,
            'itemCount': 200
        }),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['itemId'] == 3

def test_api_delete_item():
    response = app.test_client().delete('/api/Inventory/delete/3')
    data = json.loads(response.get_data(as_text=True))  
    assert "User deleted successfully" in str(response.data) 

def test_update_item():
    response = app.test_client().put(
        '/api/Inventory/update',
        data=json.dumps({ 
            'itemId' : 2,
            'itemName': "Refrigerator",
            'itemCategory': "Electronics",
            'itemPrice': 24.9,
            'itemDescription': "A refrigerator is a machine used for keeping things cold" ,
            'itemCount': 30
        }),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert data['itemCount'] == 30