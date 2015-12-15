
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

class Menu:
    def __init__(self, choices):
        self.choices = choices

    def __repr__(self):
        output = ''
        for item in self.choices:
            output += "{}: {}".format(item.number, item.text) + '\n'
        return output

    def invoke(self, number):
        for item in self.choices:
            if item.number == number:
                return item.command()

class MenuItem:
    def __init__(self, number, text, command):
        self.number = number
        self.text = text
        self.command = command

def exception(menu):
    new_menu = menu
    print(new_menu)
    while True:
        try:
            number = input('Choose a number from the menu: ')
            if int(number) > len(menu.choices):
                raise ValueError
        except ValueError:
            print('Wrong input')
            number = input('Choose a number from the menu: ')
        new_menu = new_menu.invoke(number)

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
