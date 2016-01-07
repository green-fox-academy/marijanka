class MyMagic:
    def __init__(self, strings):
        self.strings = strings

    def encoded(strings):
        output = {}
        strings = strings.lower()
        for i in strings:
            if i not in output:
                output[i] = 1
            else:
                output[i] += 1

        result = ''
        for i in strings:
            if output[i] > 1:
                result += ')'
            else:
                result += '('

        return result

        # def __init__(self, text):
        #     self.text = text.lower()
        #
        # def encode_char(self, c):
        #     return '(' if self.count(c) == 1 else ')'
        #
        # def encode(self):
        #     out = ''
        #     for c in self.text:
