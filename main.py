from manage import Manage
from user import login, register
import time
import json
import os


# with open('items.json', 'r') as f:
#     items = json.load(f)

# with open('shopping_cart.json', 'r') as f:
#     shopping_cart = json.load(f)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # Item Category{ Item ID: [Name, price]
    print("Welcome to Kimi's SuperMarket!")

    flag, admin, name = False, False, ""
    while True:
        # Login/Register
        choice_log = input("Register or Login (required): ")

        # Login Part
        if choice_log[:1].lower() == "l":
            while True:
                username = input("Enter Username: ")
                if not username:
                    break
                password = input("Enter Password: ")
                if not password:
                    break
                check = login(username, password)
                if check == "Admin" or check == "Shopper":
                    if check == "Admin":
                        admin = True
                    name = username
                    print("Login Success!")
                    time.sleep(2)
                    flag = True
                    clear()
                    break
                else:
                    print("Username or password not valid.")
                    time.sleep(2)
                    clear()

        # Registering Part
        elif choice_log[:1].lower() == "r":
            while True:
                username = input("Enter Username: ")
                if not username:
                    break
                password = input("Enter Password: ")
                if not password:
                    break
                check = register(username, password)
                if check:
                    name = username
                    print("Register Success!")
                    flag = True
                    time.sleep(2)
                    clear()
                    break
                else:
                    print("Username or password not valid.")
                    time.sleep(2)
                    clear()

        else:
            print("Not an option")

        if flag is True:
            break

    while True:
        if admin:  # If the user is an admin
            manage = Manage(name, admin=True)
            choice = input("1. Add to Shopping Cart\n"
                           "2. Remove from Shopping Cart\n"
                           "3. Search for item\n"
                           "4. Manage Items\n"
                           "Enter the number: ")
            if choice == "1":
                ...
            elif choice == "2":
                ...
            elif choice == "3":
                ...
            else:
                print("That's not an option.")
        else:  # If the user is a normal user
            manage = Manage(name, admin=False)
            choice = input("1. Add to Shopping Cart\n"
                           "2. Remove Item from Shopping Cart\n"
                           "3. Search for item\n"
                           "Enter the number: ")
            if choice == "1":
                ...
            elif choice == "2":
                ...
            elif choice == "3":
                ...


if __name__ == "__main__":
    clear()
    # print(items)
    # Item Category{ Item Name { [Item ID, price]
    # print(items['Food']['0001'])
    main()
