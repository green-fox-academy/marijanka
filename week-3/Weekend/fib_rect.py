
def perimeter(n):
    a = 0
    b = 1
    fibonacci_seq = 0
    for i in range(1, n + 2):
        a, b = b, a + b
        fibonacci_seq += a
    return fibonacci_seq * 4
