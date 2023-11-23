import sqlite3

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE if not exists customers (
                FullName Text NOT NULL,
                UserName Text PRIMARY KEY NOT NULL,
                Password Integer NOT NULL,
                Age Integer NOT NULL,
                Address Text NOT NULL,
                Gender Text NOT NULL,
                MaritalStatus Text NOT NULL
            );
        ''')
        conn.execute('''
            CREATE TABLE if not exists Inventory (
                itemId INTEGER PRIMARY KEY NOT NULL,
                itemName Text NOT NULL,
                itemCategory Text NOT NULL,
                itemPrice REAL NOT NULL,
                itemDescription Text NOT NULL,
                itemCount INTEGER NOT NULL
            );
        ''')
        conn.commit()
        print("User table created successfully")
    except:
        print("User table creation failed - Maybe table")
    finally:
        conn.close()
        
def insert_customer(customer):
    inserted_customer = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO customers (FullName, UserName, Password, Age, Address,Gender,MaritalStatus ) VALUES (?, ?, ?, ?, ?,?,?)", 
            (
                customer['FullName'], 
                customer['UserName'], 
                customer['Password'], 
                customer['Age'], 
                customer['Address'],
                customer['Gender'],
                customer['MaritalStatus']
            ) 
        )
        conn.commit()
        inserted_customer = get_customer_by_name(customer['UserName'])
    except:
        conn().rollback()
    finally:
        conn.close()
    return inserted_customer 

def delete_customer(customer_name):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from customers WHERE UserName = ?", (customer_name,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()
    return message

def update_customer(customer):
    updated_customer = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE customers SET FullName = ?, Password = ?, Age = ?, Address = ? , Gender = ? , MaritalStatus = ? WHERE UserName =?", 
            (
                customer['FullName'], 
                customer['Password'], 
                customer['Age'], 
                customer['Address'],
                customer['Gender'],
                customer['MaritalStatus'],
                customer['UserName']
            )
        )
        conn.commit()
        #return the user
        updated_customer = get_customer_by_name(customer['UserName'])
    except:
        conn.rollback()
        updated_customer = {}
    finally:
        conn.close()
    return updated_customer 

def get_customers():
    customers = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()
        # convert row objects to dictionary
        for i in rows:
            customer = {}
            customer['FullName'] = i["FullName"]
            customer['Password']= i["Password"] 
            customer['Age']= i["Age"] 
            customer['Address'] = i["Address"]
            customer['Gender'] = i["Gender"]
            customer['MaritalStatus']= i["MaritalStatus"]
            customer['UserName']= i["UserName"]
            customers.append(customer)
    except:
        customers = []
    return customers 

def get_customer_by_name(Cname):
    customer = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE UserName = ?", (Cname,))
        row = cur.fetchone()
        # convert row object to dictionary
        customer['FullName'] = row["FullName"]
        customer['Password']= row["Password"] 
        customer['Age']= row["Age"] 
        customer['Address'] = row["Address"]
        customer['Gender'] = row["Gender"]
        customer['MaritalStatus']= row["MaritalStatus"]
        customer['UserName']= row["UserName"]
    except:
        customer = {}
    return customer

def get_item(itemID):
    item = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Inventory WHERE itemId = ?", (itemID,))
        row = cur.fetchone()
        # convert row object to dictionary
        item['itemId'] = row["itemId"]
        item['itemName']= row["itemName"] 
        item['itemCategory']= row["itemCategory"] 
        item['itemPrice'] = row["itemPrice"]
        item['itemDescription'] = row["itemDescription"]
        item['itemCount']= row["itemCount"]
    except:
        item = {}
    return item

def insert_item(item):
    inserted_item = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO Inventory (itemId, itemName, itemCategory, itemPrice, itemDescription,itemCount) VALUES (?, ?, ?, ?, ?, ?)", 
            (
                item['itemId'],
                item['itemName'],
                item['itemCategory'],
                item['itemPrice'],
                item['itemDescription'],
                item['itemCount']
            ) 
        )
        conn.commit()
        inserted_item = get_item(item['itemId'])
    except:
        conn().rollback()
    finally:
        conn.close()
    return inserted_item 

def update_item(item):
    updated_item = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE Inventory SET itemName = ?, itemCategory = ?, itemPrice = ?, itemDescription = ? , itemCount = ? WHERE itemId =?", 
            (
                item['itemName'],
                item['itemCategory'],
                item['itemPrice'],
                item['itemDescription'],
                item['itemCount'],
                item['itemId']
            )
        )
        conn.commit()
        #return the user
        updated_item = get_item(item['itemId'])
    except:
        conn.rollback()
        updated_item = {}
    finally:
        conn.close()
    return updated_item  

def delete_item(itemId):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from Inventory WHERE itemId = ?", (itemId,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()
    return message 

if __name__ == "__main__":
    create_db_table()
    customer1 = {
        "FullName": "Hassan Bilal Wehbi",
        "UserName": "HBW00",
        "Password": 23141817,
        "Age": 18,
        "Address": "Beirut",
        "Gender": "Male",
        "MaritalStatus" : "Single"
    }
    customer2 = {
        "FullName": "Layal Ahmad Mohsen",
        "UserName": "lam44",
        "Password": 10000,
        "Age": 46,
        "Address": "Beirut",
        "Gender": "Female",
        "MaritalStatus" : "Maried"
    }
    # insert_customer(customer1)
    # insert_customer(customer2)
    item1 = {
        'itemId' : 1,
        'itemName': "Potato",
        'itemCategory': "Food",
        'itemPrice': 10,
        'itemDescription': "A potato is a starchy root vegetable that belongs to the nightshade family",
        'itemCount': 700,
    }
    item2 = {
        'itemId' : 2,
        'itemName': "Refrigerator",
        'itemCategory': "Electronics",
        'itemPrice': 24.9,
        'itemDescription': "A refrigerator is a machine used for keeping things cold" ,
        'itemCount': 27
    }
    # insert_item(item1)
    # insert_item(item2)