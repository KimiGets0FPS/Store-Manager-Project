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
        with open("shopping_cart.json", 'r') as sc_1:
            sc = json.load(sc_1)
            sc['Shoppers'][username] = {}
            # TODO: FIX
            with open("shopping_cart.json", 'w') as sc_2:
                json.dump(sc, sc_2, indent=4)
        return True


def change_acc_details(original_username, new_username, password):
    with open("users.json", 'r') as f:
        users = json.load(f)
        manager = False
        if original_username in users["Managers"].keys():
            manager = True
            user_info = users["Managers"][original_username]
        elif original_username in users["Shoppers"].keys():
            user_info = users["Shoppers"][original_username]

        with open("users.json", 'w') as write_users:
            if new_username:
                if manager:
                    users["Managers"].pop(original_username, None)
                    if password:
                        users["Managers"][new_username] = [password]
                    else:
                        users["Managers"][new_username] = user_info

                else:
                    users["Shoppers"].pop(original_username, None)
                    if password:
                        users["Shoppers"][new_username] = [password]
                    else:
                        users["Shoppers"][new_username] = user_info

            elif password and not new_username:
                if manager:
                    users["Managers"][original_username] = [password]

                else:
                    users["Shoppers"][original_username] = [password]
            json.dump(users, write_users, indent=4)
