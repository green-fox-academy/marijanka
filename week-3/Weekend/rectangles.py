def number_of_rectangles(m, n):

    rectangles = int((((m + 1) * m) / 2) * (((n + 1) * n) / 2))
    return rectangles

rectangles = (number_of_rectangles(4, 4))
print(rectangles)
