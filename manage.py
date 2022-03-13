import json


with open('shopping_cart.json', 'r') as c:
    shopping_cart = json.load(c)


class Manage:
    def __init__(self, username, admin=False):
        self.username = username
        self.shopping_cart = shopping_cart
        self.admin = admin

    def add_shopping_cart(self, item):
        unv_cart = self.shopping_cart  # Everyone's Shopping Cart
        cart = self.shopping_cart[self.username]
        # Add item to cart

        # If item already exists in the shopping cart
        # TODO: IMPLEMENT A WAY TO HAVE MORE
        #  THAN ONE OF THE SAME ITEM IN SOMEONE'S SHOPPING CART
        if item in self.shopping_cart[self.username].keys():
            return False

        item = item.title()

        with open("items.json", 'r') as f:
            file = json.load(f)
            flag = False
            for i in range(file.keys()):
                if item in file[i].keys():
                    flag = True
                    cart[item] = [file[i][item][0], file[i][item][1]]
            if not flag:
                return False

        # Replacing the old shopping cart with new shopping cart
        unv_cart[self.username] = cart
        new_cart = unv_cart
        with open('shopping_cart.json', 'w') as f:
            json.dump(new_cart, f)

    def delete_shopping_cart(self, item):
        cart = self.shopping_cart[self.username]
        # Check if item is in cart, then delete that item if it exists

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
