from flask import Flask, request, jsonify 
from flask_cors import CORS
from databaseFunctions import * 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/customers/add', methods=['POST'])
def api_add_customer():
    """Register a new customer. The service should save the following information:
            o Full name
            o Username and password. The username should be unique. The service should check 
            that the username is unique and return an error if it is taken.
            o Age
            o Address
            o Gender
            o Marital status

    Returns:
        jsonify: customer added
    """
    customer = request.get_json()
    return jsonify(insert_customer(customer))

@app.route('/api/customers/delete/<Cname>', methods = ['DELETE'])
def api_delete_customer(Cname):
    """Delete customer

    Args:
        customer_id (integer): customer's id 

    Returns:
        jsonify: dictionary of the attributes of the deleted customer
    """
    return jsonify(delete_customer(Cname))

@app.route('/api/customers/update', methods = ['PUT'])
def api_update_customer():
    """Update customer information. It should update one or many fields related to the customer information.

    Returns:
        jsonify: updated user dictionary of attributes
    """
    customer = request.get_json()
    return jsonify(update_customer(customer))

@app.route('/api/customers', methods=['GET'])
def api_get_customers():
    """ Get all customers
    
    Returns:
        jsonify: returns all customes 
    """
    return jsonify(get_customers())

@app.route('/api/customers/<Cname>', methods=['GET'])
def api_get_customer(Cname):
    """_summary_

    Args:
        Cname (_type_): _description_

    Returns:
        _type_: _description_
    """
    return jsonify(get_customer_by_name(Cname))

# ask professor about them 
def charge_customer():
    pass 

def deduce_money():
    pass

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() #run app
