class MySuperString:
    def __init__(self, my_string):
        self.my_string = my_string

    def space_change(self):
        result = ''
        for i in self.my_string:
            if i == ' ':
                result =  result + '_'
            else:
                result = result + i
        return result
