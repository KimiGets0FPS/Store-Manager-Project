import json
import os
import time


with open('shopping_cart.json', 'r') as c:
    shopping_cart = json.load(c)

with open('items.json', 'r') as it:
    items = json.load(it)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_item(item_name, item_cat, price, admin):
    if admin:
        # Adding an item to the supermarket
        if item_name in items[item_cat].keys():
            return None
        last_item = list(items[item_cat].items())[-1]
        last_id = last_item[1][0]
        items[item_cat][item_name] = [str(int(last_id)+1), price]
        with open("items.json", 'w') as f:
            json.dump(items, f, indent=4)
        print(type(last_item))
        print(last_item)
        return True
    return False


def delete_item(item_name, item_cat, admin):
    if admin:
        # Making the item unavailable
        if item_name in items[item_cat]:
            return True
    return False


class Manage:
    def __init__(self, username, admin=False):
        self.username = username
        self.items = items
        self.shopping_cart = shopping_cart
        self.admin = admin

    def add_shopping_cart(self, item):
        unv_cart = self.shopping_cart  # Everyone's Shopping Cart
        cart = self.shopping_cart[self.username]

        # If item already exists in the shopping cart
        # TODO: IMPLEMENT A WAY TO HAVE MORE
        #  THAN ONE OF THE SAME ITEM IN SOMEONE'S SHOPPING CART
        if item in self.shopping_cart[self.username].keys():
            return False

        # Checking if item exists in items.json
        flag = False
        for categories in self.items.keys():
            for i in range(len(self.items[categories])):
                if item == self.items[categories][i]["Name"].title():
                    flag = True
                    cart[item] = [self.items[categories][i]["ID"], self.items[categories][i]["Price"]]
                    break
        if flag is False:
            return None

        # Replacing the old shopping cart with new shopping cart
        unv_cart[self.username] = cart
        with open('shopping_cart.json', 'w') as f:
            json.dump(unv_cart, f, indent=4)
        return True

    def delete_shopping_cart(self, item):
        new_unv_cart = self.shopping_cart
        cart = self.shopping_cart[self.username]
        # Check if item is in cart, then delete that item if it exists
        flag = False
        for categories in self.items.keys():
            for i in range(len(self.items[categories])):
                if item == self.items[categories][i]["Name"]:
                    flag = True
                    cart[item] = [self.items[categories][i]["ID"], self.items[categories][i]["Price"]]
                    break
        if not flag:
            return False

        if item not in cart:
            return None
        cart.pop(item)
        new_unv_cart[self.username] = cart
        with open('shopping_cart.json', 'w') as f:
            json.dump(new_unv_cart, f, indent=4)
            return True

    def view_shopping_cart(self):
        cart = self.shopping_cart[self.username]
        if cart == {}:
            return False
        return cart

    def search_item(self, item):
        search_results = []
        for category in self.items.keys():
            for item_name in self.items[category]:
                if item in item_name.lower():
                    search_results.append([item_name, self.items[category][item_name][1]])
        if search_results:
            return search_results
        return False

    def manage_item(self, choice):
        while True:
            item_name = input("Enter a name for the item: ").title()
            if not item_name:
                break
            item_cat = input("Enter a category for the item: ").title()
            if not item_cat:
                break
            if choice == "1":
                price = input(f"Enter the price for {item_name}: ")
                if not price:
                    print("Must enter price!")
                else:
                    managed = add_item(item_name, item_cat, price, self.admin)
                    if managed is None:
                        print("That is already an item!")
                        time.sleep(2)
                        clear()

            elif choice == "2":
                managed = delete_item(item_name, item_cat, self.admin)
                if managed:
                    print("Success!")
                    time.sleep(2)
                    clear()
        print("Exiting...")
        time.sleep(1)
        clear()
