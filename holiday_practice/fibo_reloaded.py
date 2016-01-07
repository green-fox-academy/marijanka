def perimeter(n):
    a = 0
    b = 1

    for i in range(0, n-1):
        a, b = b, a + b
    print(float(a))

perimeter(0)
perimeter(1)
perimeter(2)
perimeter(3)
