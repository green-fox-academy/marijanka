i = 0
while i < 100:

    if '3' in str(i) and '5' in str(i):
        print(i, "FIZZBUZZ")
    elif '5' in str(i):
        print(i, "BUZZ")
    elif '3' in str(i):
        print(i, "FIZZ")
    else:
        print(i)
    i += 1
