import json



class User:
    def __init__(self):
        ...

    def login(self, username, password):
        with open("users.json", 'r') as f:
            users = json.load(f)
        if username in users["Managers"].keys():
            if users["Managers"][username][0] == password:
                return "Admin"
        if username in users["Shoppers"].keys():
            if users["Shoppers"][username][0] == password:
                return "Shopper"
        return False

    def register(self, username, password):
        with open("users.json", 'r') as f:
            file = json.load(f)
            if username in file["Managers"].keys() or username in file["Shoppers"].keys():
                return False
            file["Shoppers"][username] = [password]
            with open("users.json", 'w') as f:
                json.dump(file, f)
            return True
