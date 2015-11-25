class BankAccount:
    def __init__(self, name, amount = 0):
        self.name = name
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
