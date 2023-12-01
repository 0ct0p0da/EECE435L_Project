import pytest
from service3_apis import *
from flask import json

def test_api_get_good_list():
    response = app.test_client().post(
        '/api/goods/list',
        data=json.dumps({
            "itemName": "Shampoo",
            "itemPrice": "25",
        }),
        data=json.dumps({
            "itemName": "Croissant",
            "itemPrice": "10",
        }),
        data=json.dumps({
            "itemName": "Milk",
            "itemPrice": "5",
        }),

        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['itemName'] == "Shampoo" ################## NOT CORRECT, I want to check if a list is returned

def test_api_get_good_details(): ####################################
    response = app.test_client().post(
        '/api/goods/list',
        data=json.dumps({
            "itemName": "Shampoo",
            "itemPrice": "25",
            "itemId": "001",
            "itemCategory": "Hygiene",
            "itemDescription" : "A shampoo that works for all parts of the body"
            "itemCount": "20",
        }),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['itemName'] == "Shampoo"

def test_api_sell_good():
    response = app.test_client().post(
        '/api/goods/list',
        data=json.dumps({
            "itemName": "Shampoo",
            "itemPrice": "25",
            "itemId": "001",
            "itemCategory": "Hygiene",
            "itemDescription" : "A shampoo that works for all parts of the body"
            "itemCount": "20",
        }),
        content_type='application/json',
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200