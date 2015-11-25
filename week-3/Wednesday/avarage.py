class MyNumberClass:
    def avarage(self, list):
        count = 0
        n = len(list)
        if n == 0:
            return print('it is not good')
        for i in list:
            count += i

        return count / n
