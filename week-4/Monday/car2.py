class Car:
    def __init__(self, color, car_type, km):
        if type(color) != str:
            raise Exception('Color is a string')
        self.color = color
        self.type = type
        self.km = km

    def ride(self, km):
        self.km += km

    def getMiles(self):
        return self.km * 0.6213

tesla = Car('pink', 'Tesla S', 1200)

lada = Car('blue', 'Lada 1200', 40000)

tesla.ride(220)
print(tesla.km)
print(tesla.getMiles())
