from menu import *

def main_menu():
     items = [
       MenuItem("1", "New Game", main_submenu),
       MenuItem("2", "Load Game", ''),
       MenuItem("0", "Exit", exit)
     ]
     return Menu(items)

def new_game_submenu():
    items = [
        MenuItem("1", "Reenter name", main_submenu),
        MenuItem("2", "Continue", ''),
        MenuItem("3", "Save", ''),
        MenuItem("0", "Quit", main_quit_submenu)
    ]
    return Menu(items)

def quit_submenu():
    items = [
        MenuItem("1", "Resume", ''),
        MenuItem("2", "Save and Quit", ''),
        MenuItem("0", "Quit without Save", exit)
    ]
    return Menu(items)

def exception(menu):
    new_menu = menu
    print(new_menu)
    while True:
        try:
            number = input('Choose a number from the menu: ')
            if int(number) > len(menu.choices):
                raise ValueError
            new_menu = new_menu.invoke(number)
        except ValueError:
            print('Wrong input')

def main_main_menu():
    menu = main_menu()
    exception(menu)

def main_submenu():
    user_name = input('Please give your name(min. 5 character): ')
    print(user_name)
    if len(user_name) < 5:
        main_submenu()
    else:
        menu = new_game_submenu()
        exception(menu)

def main_quit_submenu():
    menu = quit_submenu()
    exception(menu)
