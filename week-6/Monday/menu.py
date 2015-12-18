from exception import PocsolyszeError

class MenuItem:
    def __init__(self, number, text, command):
        self.number = number
        self.text = text
        self.command = command

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

def exception(menu):
    last_last_menu = None
    last_menu = None
    new_menu = menu
    while True:
        try:
            print(new_menu)
            number = input('Choose a number from the menu: ')
            if int(number) > len(menu.choices):
                raise ValueError
            last_last_menu = last_menu
            last_menu = new_menu
            new_menu = new_menu.invoke(number)
        except ValueError:
            print('Wrong input')
        except PocsolyszeError:
            new_menu = last_last_menu
