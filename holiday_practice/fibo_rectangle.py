def sqInRect(lng, wdth):
    fibo = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    sequence = []
    if lng > wdth:
        for i in range(len(fibo)):
            if wdth == fibo[i] and lng == fibo[i+1]:
                for i in range(i+1):
                    sequence.append(fibo[i])
                print(sequence[::-1])
                break
        else:
            print(None)

    elif lng < wdth:
        for i in fibo:
            if fibo[i] == lng and fibo[i+1] == wdth:
                for i in range(i+1):
                    sequence.append(fibo[i])
                print(sequence[::-1])
                break
        else:
            print(None)

    else:
        print(None)

sqInRect(5, 3)
sqInRect(8, 13)
sqInRect(5, 5)
sqInRect(9, 5)
