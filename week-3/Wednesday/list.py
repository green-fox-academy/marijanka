class MySuperString:
    def __init__(self, my_string):
        self.my_string = my_string

    def reverse1(self):
        z = len(self.my_string)
        reversed = ""
            reversed = self.my_string[n] + reversed
        for n in range(z):
        return reversed

    def reverse2(self):
        z = len(self.my_string)
        reversed = ""
        for n in range(z-1, -1, -1):
            reversed += self.my_string[n]
        return reversed

    def reverse(self):
        reversed = ""
        for i in self.my_string:
            reserved = i + reserved
        return reversed
