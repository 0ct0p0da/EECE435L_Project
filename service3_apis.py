"""
Display available goods: this API should return a list of 
     Good name
     Price

Get goods details: This API should return full information related to a specific good

Sale: when a customer makes a sale, this API takes the name of good, the customer username, 
checks if the user has enough money to purchase and if the good is still available. If all the 
conditions are met, the service should deduce the money from the customer wallet and 
decrease the count of the purchased good from the database.

You should find a way to save all the historical purchases made by a customer
"""

from flask import Flask, request, jsonify
from flask_cors import CORS 
import sqlite3

print("Imported libs successfully")

def connect_to_db():
 conn = sqlite3.connect('database.db')
 return conn

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.run()

@app.route('/api/goods/list', methods=['GET'])
def api_get_good_list():
    """ Display available goods: this API should return a list of 
        - Good name
        - Price 
    """
    return jsonify(get_good_list())

@app.route('/api/goods/details', methods=['GET'])
def api_get_good_details():
    """Full information Relating to a specific good"""
    return jsonify(get_good_details())

@app.route('/api/goods/sell', methods=['DELETE'])
def api_sell_good():
    """This API sells a good:
        - Takes the name of the good and the customer usename
        - Checks whether the item is available
        - Checks whether the custonmer has enough money to buy
        - Reduces the Count of the good
        - Duduces money from the customer
    """
    return jsonify(sell_good())


