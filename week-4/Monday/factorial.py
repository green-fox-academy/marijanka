numbers = 5

def fact(num):
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    return factorial

numbers = fact(numbers)
print(numbers)

def fact2(num):
    factorial = 1
    for n in range(1, numbers +1):
        factorial *=n
    return factorial

numbers = fact2(numbers)
print(numbers)

def fact3(num):
    if n == 0:
        return 1
    else:
        return n * fakt3(n-1)

numbers = fact3(numbers)
print(numbers)
