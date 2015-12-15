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
