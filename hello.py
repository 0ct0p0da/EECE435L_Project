from flask import Flask, request, jsonify
from flask_cors import CORS 
import sqlite3
print("Imported libs successfully")

def connect_to_db():
 conn = sqlite3.connect('database.db')
 return conn

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/goods/add', methods=['POST'])
def api_add_good():
    return jsonify(add_good())

@app.route('/api/goods/delete', methods=['DELETE'])
def api_delete_good():
    return jsonify(delete_good())

@app.route('/api/goods/update', methods=['PUT'])
def api_update_good():
    return jsonify(update_good())


