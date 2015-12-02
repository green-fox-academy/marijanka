def fibo(signature, n):
    j = len(signature)
    a = signature[j-2]
    b = signature[j-1]
    numbers = []
    for i in range(1, n+2-j):
        a, b = b, a + b
        numbers.append(a)
    return numbers

def Xbonacci(signature, n):
    fibonacci = fibo(signature, n)
    fibonacci.pop(1)
    result = signature + fibonacci
    return result

output = Xbonacci([0,0,0,0,1],10)
print(output)
