import json



with open("items.json", 'r') as f:
    items = json.load(f)


class Manage:
    def __init__(self):
        ...

    def add_shopping_cart(self, item):
        ...

    def delete_shopping_cart(self, item):
        ...