n = 5
a = 0
b = 1
numbers = []
for i in range(0, n):
    a, b = b, a + b
    numbers.append(a)
print(numbers)
