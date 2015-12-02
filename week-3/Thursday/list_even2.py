numbers = [1, 2, 3, 4, 5, 6, 7, 8]
output = []

def even(list):
    for i in list:
        if i % 2 == 0:
            output.append(i)
    return output

output = filter_even(numbers)

print(output)
