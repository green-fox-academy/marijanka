def sqInRect(lng, wdth):
    if wdth > lng:
        n = wdth
    else:
        n = lng
    a = 0
    b = 1
    fibonacci_seq = []
    for i in range(1, n+1):
        a, b = b, a + b
        fibonacci_seq.append(a)
    return lng, wdth, fibonacci_seq[::-1]

def result():
    x, z, lista = sqInRect(lng, wdth)
    if (list[0] == z and list[1] == x) or (list[0] == x and list[1] == z):
        return list.pop(1)
    else:
        return None
