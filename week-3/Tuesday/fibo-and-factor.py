def fibo(n):
a = 0
b = 1
numbers = []
for i in range(0, n):
    a, b = b, a + b
    numbers.append(a)
return numbers

factors = []

def factors():
    if n == 0:
        return 1
    else:
        return n * factors(n-1)
