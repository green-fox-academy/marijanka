def get_fizz(number):
    if number % 3 == 0:
        return 'fizz'
    else:
        return number

def fizz_buzz(minimum, maximum):
    n = minimum
    while n <= maximum:
        print(get_fizz(n))
        n += 1


fizz_buzz(1, 50)

def is_fizz(number):
    return number % 3 == 0 or '3' in str(number)

def is_buzz(number):
    return number % 5 == 0 or '5' in str(number)

def fizz_buzz1(minimum, maximum):
    n = minimum
    while n <= maximum:
        if is_buzz(n) and is_fizz(n):
            print('fizzbuzz')
        elif is_fizz(n):
            print('fizz')
        elif is_buzz(n):
            print('buzz')
        else:
            print(n)
        n += 1

fizz_buzz1(1, 50)

def is_fizzish(number, base):
    return number % base == 0 or str(base) in str(number)

def fizz_buzz2(minimum, maximum = 100):
    n = minimum
    fizz_number = 3
    buzz_number = 5
    while n <= maximum:
        if is_fizzish(n, fizz_number) and is_fizzish(n, buzz_number):
            print('fizzbuzz')
        elif is_fizzish(n, fizz_number):
            print('fizz')
        elif is_fizzish(n, buzz_number):
            print('buzz')
        else:
            print(n)
        n += 1

fizz_buzz2(1, 100)
