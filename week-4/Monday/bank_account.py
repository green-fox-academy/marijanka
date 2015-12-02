class Bank_account:
    def __init__(self, name, balance):
        if type(balance) != int:
            raise Exception('Balance is a float')
        if type(name) != str:
            raise Exception('Name is a string')
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount

    def receive(self, amount):
        self.balance += amount

    def print_balance(self):
        print('Balance of:')
        print(self.name)
        print('is: ')
        print(self.balance)

    def transfer(self, name_to, amount):
        self.balance -= amount
        name_to.balance += amount

tojas = Bank_account('Tamas Kokeny', 46)
feri = Bank_account('Feri *', 7000000)

tojas.receive(130000)
tojas.transfer(feri, 10000)
tojas.print_balance()
