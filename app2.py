from flask import Flask, request, jsonify 
from flask_cors import CORS
from database.functions import insert_item,delete_item,update_item

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/Inventory/add', methods=['POST'])
def api_add_item():
    """Adding items:
        o Name
        o Category (food, clothes, accessories, electronics)
        o Price per item
        o Description
        o Count of available items in stock

    Returns:
        jsonify: dictionary of the item added
    """
    item = request.get_json()
    return jsonify(insert_item(item))

@app.route('/api/Inventory/delete/<itemId>', methods = ['DELETE'])
def api_delete_item(itemId):
    """Delete item

    Args:
        itemId (integer): item's id 

    Returns:
        jsonify: dictionary of the attributes of the deleted item
    """
    return jsonify(delete_item(itemId))

@app.route('/api/Inventory/update', methods = ['PUT'])
def api_update_item():
    """Updating items: updating fields related to a specific item


    Returns:
        jsonify: updated item dictionary of attributes
    """
    item = request.get_json()
    return jsonify(update_item(item))

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() #run app
