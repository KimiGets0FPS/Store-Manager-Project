from PySimpleGUI import *  # Makes my life so much easier
import time


def main_window():
    add_sc = [
        [InputText([])]
    ]
    tab1 = Tab("Add Item to Shopping Cart: ", [[Frame('Item you want to add', add_sc)]])

    layout = [[tab1]]
    window = Window(title="Kimi's Supermarket", layout=layout, resizable=True)
    return window


def main():
    window = main_window()
    while True:
        event, values = window.read(timeout=5)
        if event == WIN_CLOSE_ATTEMPTED_EVENT:
            return


if __name__ == "__main__":
    main()
