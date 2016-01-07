def pascal(p):
    row1 = [1]
    row2 = [1, 1]
    trg = [row1, row2]
    r = []
    result = []
    if p == 1:
        print(row1)
    elif p == 2:
        print(trg)
    else:
        for i in range(2, p):
            trg.append([1]*i)
            for n in range(1, i):
                trg[i][n] = (trg[i-1][n-1]+trg[i-1][n])
            trg[i].append(1)
        for i in range(len(trg)):
            for a in trg[i]:
                num = a
                r.append(num)
            result.append(r)
            r = []
        print(result)
pascal(1)
pascal(2)
pascal(3)
pascal(4)
