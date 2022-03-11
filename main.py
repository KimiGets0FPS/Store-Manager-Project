from manage import Manage
from user import User
import time
import json
import os


manage = Manage()
user = User()

with open('items.json', 'r') as f:
    items = json.load(f)

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')



def main():
    # Item Category{ Item ID { [Name, price]
    print("Welcome to Kimi's SuperMarket!")
    # Login
    flag, admin = False, False
    while True:
        choice_log = input("Register or Login (required): ")
        if choice_log[:1].lower() == "l":
            while True:
                username = input("Enter Username: ")
                if not username:
                    break
                password = input("Enter Password: ")
                if not password:
                    break
                check = user.login(username, password)
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
                    time.sleep(3)
                    clear()

        elif choice_log[:1].lower() == "r":
            while True:
                username = input("Enter Username: ")
                if not username:
                    break
                password = input("Enter Pasword: ")
                if not password:
                    break
                check = user.register(username, password)
                if check:
                    print("Register Success!")
                    flag = True
                    time.sleep(2)
                    clear()
                    break
                else:
                    print("Username or password not valid.")
                    time.sleep(3)
                    clear()
        else:
            print("Not an option")

        if flag == True:
            break

    while True:
        if admin:  # If the user is an admin
            choice = input("1. Add to Shopping Cart\n2. Remove from Shopping Cart\n3. \nEnter the number: ")
        else:  # If the user is a normal user
            choice = input("1. Add to Shopping Cart\n2. Remove Item from Shopping Cart\n3. ")
        


if __name__ == "__main__":
    clear()
    # print(items)
    # Item Category{ Item ID { [Name, price]
    # print(items['Food']['0001'])
    main()
