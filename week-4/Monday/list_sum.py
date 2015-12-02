numbers = [4, 5, 6, 7, 8, 9]

a = sum(numbers)
print(a)

def sum(num_list):
    num = 0
    for i in num_list:
        num += i
    return num

numbers = sum(numbers)
print(numbers)
