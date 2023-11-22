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

if __name__ == "__main__":
    create_db_table()
    customer = {
        "FullName": "Hassan Bilal Wehbi",
        "UserName": "HBW00",
        "Password": 23141817,
        "Age": 18,
        "Address": "Beirut",
        "Gender": "Male",
        "MaritalStatus" : "Single"
    }
    insert_customer(customer)