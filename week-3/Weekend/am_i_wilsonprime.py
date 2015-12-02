import math

def am_i_wilson(n):
    n = int(n)
    if n <= 0:
        return False
    else:
        a = 2
        while a <= n ** 0.5:
            if (n % a == 0):
                return False
            a += 1
        else:
            p = (math.factorial(n-1)) + 1
            g = n * n
            if p % g == 0:
                 return True
            else:
                 return False

result = am_i_wilson(563)
print(result)

# def am_i_wilson(n):
#     return n == 5 or n == 13 or n == 563 or n == 5971 or n == 558771 or n == 1964215 or n == 8121909 or n == 12326713 or n == 23025711 or n == 26921605 or n == 341569806 or n == 399292158
