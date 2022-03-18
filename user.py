import json


def login(username, password):
    with open("users.json", 'r') as f:
        users = json.load(f)
    if username in users["Managers"].keys():
        if users["Managers"][username][0] == password:
            return "Admin"
    if username in users["Shoppers"].keys():
        if users["Shoppers"][username][0] == password:
            return "Shopper"
    return False


def register(username, password):
    with open("users.json", 'r') as f:
        users = json.load(f)
        if username in users["Managers"].keys() or username in users["Shoppers"].keys():
            return False
        users["Shoppers"][username] = [password]
        with open("users.json", 'w') as user:
            json.dump(users, user, indent=4)
        with open("shopping_cart.json", 'w') as sc:
            json.dump({username: {}}, sc, indent=4)
        return True
