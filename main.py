import os
import time
import json
from termcolor import cprint

from manage import Manage
from user import login, register


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Trying to fix the json file if there aren't any shopping cart users
# For some reason, it fixes itself AFTER a restart on the script
# I can't fix this in any way because Python is just like this so ye :p
with open('shopping_cart.json', 'r') as shopping_cart:
    shopping_cart = json.load(shopping_cart)
    if not shopping_cart:
        with open('shopping_cart.json', 'w') as f:
            with open('users.json', 'r') as users:
                users = json.load(users)
                stuff = {}
                for user in users["Managers"].keys():
                    stuff[user] = {}
                for user in users["Shoppers"].keys():
                    stuff[user] = {}
            json.dump(stuff, f, indent=4)


def main():
    cprint("Welcome to Kimi's SuperMarket!", color='blue')
    time.sleep(1)

    flag, admin, name = False, False, ""
    while True:
        # Login/Register
        choice_log = input("Register or Login (required): ")
        if choice_log:
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
                        cprint("Register Success!", color='green')
                        flag = True
                        time.sleep(2)
                        clear()
                        break
                    else:
                        cprint("Username or password not valid.", color='red')
                        time.sleep(2)
                        clear()

            else:
                print("Not an option")

        else:
            return

        if flag is True:
            break

    while True:
        # TODO: ADMIN -> SHOPPER MODE WHEN (AND VICE VERSA)???
        if admin:  # If the user is an admin
            manage = Manage(name, admin=True)
            while True:
                choice = input("Press Enter anytime to exit\n"
                               "1. Add to Shopping Cart\n"
                               "2. Remove from Shopping Cart\n"
                               "3. View Your Shopping Cart\n"
                               "4. Search for item\n"
                               "5. Manage Items\n"
                               "Enter the number: ")
                if choice:
                    if choice == "1":
                        while True:
                            item = input("Enter item name to add: ")
                            item = item.title()
                            if item:
                                managed = manage.add_shopping_cart(item)
                                if managed:
                                    cprint(f"{item.title()} successfully added to shopping cart!", color='green')
                                elif managed is None:
                                    cprint("There's no such item (very sensitive system)!", color='red')
                                elif managed is False:
                                    print("You already have this item in your shopping cart!")
                                time.sleep(2)
                                clear()
                                break
                            else:
                                clear()
                                break

                    elif choice == "2":
                        while True:
                            item = input("Enter item name to remove: ")
                            item = item.title()
                            if item:
                                managed = manage.delete_shopping_cart(item)
                                if managed is True:
                                    print(f"{item} was successfully removed to your shopping cart!")
                                    time.sleep(2)
                                    clear()
                                    break
                                elif managed is False:
                                    print("There's no such item (very sensitive system)!")
                                    time.sleep(2)
                                    clear()
                                elif managed is None:
                                    print("You don't have that item in your shopping cart!")
                                    time.sleep(2)
                                    clear()

                            else:
                                clear()
                                break

                    elif choice == "3":
                        managed = manage.view_shopping_cart()
                        if managed:
                            clear()
                            print("Your Shopping Cart:")
                            for i in managed.keys():
                                print(f"{i}: ${managed[i][1]}")
                            input("Press Enter to Continue...")
                            clear()

                        else:
                            cprint("You don't have anything in your shopping cart!", color='yellow')
                            time.sleep(2)

                    elif choice == "4":
                        while True:
                            item = input("Enter prefix/item name to search (be slightly specific): ")
                            if item:
                                managed = manage.search_item(item)
                                if managed:
                                    for i in range(len(managed)):
                                        print(f"{i+1}. {managed[i][0]}: ${managed[i][1]}")
                                else:
                                    cprint("No related results!", color='yellow')
                            else:
                                break

                    elif choice == "5":
                        while True:
                            choice = input("1. Add item\n2. Delete item\nChoice: ")
                            if not choice:
                                break
                            if choice == "1" or choice == "2":
                                manage.manage_item(choice)
                                clear()
                            else:
                                cprint("Not an option!", color='yellow')
                                time.sleep(2)
                            time.sleep(2)
                            clear()

                    else:
                        cprint("That's not an option.", color='red')
                else:
                    return

        else:  # If the user is a normal user
            manage = Manage(name, admin=False)
            while True:
                choice = input("1. Add to Shopping Cart\n"
                               "2. Remove Item from Shopping Cart\n"
                               "3. View Your Shopping Cart\n"
                               "4. Search for item\n"
                               "Enter the number: ")

                if choice:

                    if choice == "1":
                        while True:
                            item = input("Enter Item name: ")
                            if item:
                                managed = manage.add_shopping_cart(item)
                                if managed:
                                    print(f"{item.title()} successfully added to shopping cart!")
                                else:
                                    print("There's no such item (very sensitive system)!")
                                time.sleep(2)
                                clear()
                                break

                            else:
                                break

                    elif choice == "2":
                        while True:
                            item = input("Enter item name to remove: ")
                            item = item.title()
                            if item:
                                managed = manage.delete_shopping_cart(item)
                                if managed is True:
                                    print(f"{item} was successfully removed to your shopping cart!")
                                    time.sleep(2)
                                    clear()
                                    break
                                elif managed is False:
                                    print("There's no such item (very sensitive system)!")
                                    time.sleep(2)
                                    clear()
                                elif managed is None:
                                    print("You don't have that item in your shopping cart!")
                                    time.sleep(2)
                                    clear()

                            else:
                                clear()
                                break

                    elif choice == "3":
                        managed = manage.view_shopping_cart()
                        if managed:
                            clear()
                            print("Your Shopping Cart:")
                            for i in managed.keys():
                                print(f"{i}: ${managed[i][1]}")
                            input("Press Enter to Continue...")
                            clear()

                        else:
                            cprint("You don't have anything in your shopping cart!", color='yellow')
                            time.sleep(2)

                    elif choice == "4":
                        while True:
                            item = input("Enter prefix/item name to search (be slightly specific): ")
                            if item:
                                managed = manage.search_item(item)
                                if managed:
                                    for i in range(len(managed)):
                                        cprint(f"{i+1}. {managed[i][0]}: ${managed[i][1]}", color='green')
                                else:
                                    cprint("No related results!", color='yellow')
                            else:
                                break

                    else:
                        cprint("That's not an option!", color='red')
                else:
                    return
                clear()


if __name__ == "__main__":
    clear()
    main()
    clear()
    print("Thank You!")
    time.sleep(2)
    clear()
