def is_big_number1(number):
    return number > 100

print(is_big_number1(104))

def is_big_number(number):
    return number > 100

def print_bigness(number):
    print('I am gonna decide on: ')
    print number
    if is_big_number(number):
        print('is soo big!!!')
    else:
        print('wrr')

print(is_big_number(2))
print(print_bigness(104))
