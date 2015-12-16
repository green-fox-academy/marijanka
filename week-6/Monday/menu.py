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
            new_menu = new_menu.invoke(number)
        except ValueError:
            print('Wrong input')
