def greet1(name, hi):
    print(hi + ", " + name)

greet1("Cuki", "Hello")
greet1("Cuki", "Szia")


def greet2(name, hi):
    if hi is None:
        hi = "Hello"
    print(hi + ", " + name)

greet2("Cuki", "Hello")
greet2("Cuki", "Szia")
greet2("Cuki", None)

def greet3(name, hi = None):
    print(hi + ", " + name)

greet3("Cuki", "Hello")
greet3("Cuki", "Szia")
greet3("Cuki")
