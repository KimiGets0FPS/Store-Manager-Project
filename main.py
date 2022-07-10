import os
import time
import json
from termcolor import cprint

from manage import Manage
from user import login, register, change_acc_details


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


def admin_panel(name, password):
    manage = Manage(name, admin=True)
    while True:
        choice = input("Press Enter anytime to exit\n"
                       "1. Search for item\n"
                       "2. Manage Items\n"
                       "3. Manage Account\n"
                       "4. Switch to Shopping mode\n"
                       "Enter the number: ")
        if choice:

            if choice == "1":
                while True:
                    item = input("Enter prefix/item name to search (be slightly specific): ")
                    if item:
                        managed = manage.search_item(item)
                        if managed:
                            for i in range(len(managed)):
                                print(f"{i + 1}. {managed[i][0]}: ${managed[i][1]}")
                        else:
                            cprint("No related results!", color='yellow')
                    else:
                        break

            elif choice == "2":
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

            elif choice == "3":
                print(f"Username: {name}\nPassword: {password}")
                new_username = input("New Username:")
                new_password = input("New Password: ")
                if new_username or new_password:
                    change_acc_details(name, new_username, new_password)
                    cprint("Success!", color="green")
                    time.sleep(2)
                    clear()

            elif choice == "4":
                return "switch_mode"

            else:
                cprint("That's not an option.", color='red')
        else:
            return


def shopper_panel(name, password):
    manage = Manage(name, admin=False)
    while True:
        choice = input("1. Add to Shopping Cart\n"
                       "2. Remove Item from Shopping Cart\n"
                       "3. View Your Shopping Cart\n"
                       "4. Search for item\n"
                       "5. Manage Account\n"
                       "6. Switch to Admin mode (admin account required)\n"
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
                                cprint(f"{i + 1}. {managed[i][0]}: ${managed[i][1]}", color='green')
                        else:
                            cprint("No related results!", color='yellow')
                    else:
                        break

            elif choice == "5":
                print(f"Username: {name}\nPassword: {password}")
                new_username = input("New Username:")
                new_password = input("New Password: ")
                if new_username or new_password:
                    change_acc_details(name, new_username, new_password)
                    cprint("Success!", color="green")
                    time.sleep(2)
                    clear()

            elif choice == "6":
                with open("users.json", 'r') as user_file:
                    users_ = json.load(user_file)
                    if name in users_["Managers"].keys():
                        return "switch_mode"
                    else:
                        cprint("You don't have permission!", color="red")
                        input("Press Enter to continue...")

            else:
                cprint("That's not an option!", color='red')
        else:
            return
        clear()


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

    switch = False
    while True:
        if admin and switch is False:  # If the user is an admin
            # Pycharm is dumb
            # noinspection PyUnboundLocalVariable
            admin = admin_panel(username, password)
            if admin == "switch_mode":
                switch = True
                print("Switching...")
                time.sleep(1)
                clear()

        elif switch is True:  # If the user is a normal user
            shopper = shopper_panel(username, password)
            if shopper == "switch_mode" and switch is True:
                switch = False
                print("Switching...")
                time.sleep(1)
                clear()


if __name__ == "__main__":
    clear()
    main()
    clear()
    print("Thank You!")
    time.sleep(2)
    clear()
