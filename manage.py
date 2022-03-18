import json


with open('shopping_cart.json', 'r') as c:
    shopping_cart = json.load(c)

with open('items.json', 'r') as it:
    items = json.load(it)


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
            if item in self.items[categories].keys():
                flag = True
                cart[item] = [self.items[categories][item][0], self.items[categories][item][1]]
                break
        if not flag:
            return False

        # Replacing the old shopping cart with new shopping cart
        unv_cart[self.username] = cart
        with open('shopping_cart.json', 'w') as f:
            json.dump(unv_cart, f)
        return True

    def delete_shopping_cart(self, item):
        new_unv_cart = self.shopping_cart
        cart = self.shopping_cart[self.username]
        # Check if item is in cart, then delete that item if it exists
        flag = False
        for categories in self.items.keys():
            if item in self.items[categories].keys():
                flag = True
                cart[item] = [self.items[categories][item][0], self.items[categories][item][1]]
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

    def delete_item(self, item):
        if self.admin:
            # Making the item unavailable
            ...
        return False

    def add_item(self, item):
        if self.admin:
            # Adding an item to the supermarket
            ...
        return False
