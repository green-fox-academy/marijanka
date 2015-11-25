class MySuperString:
    def __init__(self, my_string):
        self.my_string = my_string

    def Count(self, char):
        implement = 0
        for ch in self.my_string:
            if char == ch:
                implement += 1
        return implement
