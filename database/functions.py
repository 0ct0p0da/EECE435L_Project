import sqlite3

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

def get_good_list():
    goods = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT itemName, itemPrice FROM Inventory")
        rows = cur.fetchall()
        # convert row objects to dictionary
        for i in rows:
            good = {}
            good['itemName'] = i["itemName"]
            good['itemPrice']= i["itemPrice"] 
            good.append(goods)
    except:
        goods = []
    return goods

def get_good_details(itemName):
    Details = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM Inventory WHERE itemName = {itemName}")
        item = cur.fetchall()
        Details["itemId"] = item["itemId"]
        Details["itemName"] = item["itemName"]
        Details["itemCategory"] = item["itemCategory"]
        Details["itemPrice"] = item["itemPrice"]
        Details["itemDescription"] = item["itemDescription"]
        Details["itemCount"] = item["itemCount"]
    except:
        Details = []
    return Details


def sell_good(itemName, FullName, count):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute(f"SELECT * FROM Inventory WHERE itemName = {itemName}")
        item = conn.fetchall()
        conn.execute(f"SELECT * FROM Customers WHERE FullName = {FullName}")
        buyer  = conn.fetchall
        if item["itemCount"] == 0:
            message["error"] = f"Sorry,  We do not have any of {itemName} "
        if item["itemCount"] < count:
            item["itemCount"] = itemcount
            message["error"] = f"Sorry, we do not have {count} of {itemName} in the inventory, we only have {itemcount}"
        if buyer["Wallet"] < count*item["itemPrice"]:
            message["error"] = f"Sorry, you do not have enough money to buy {count} of {itemName}"
    except:
        message = {}
    return message