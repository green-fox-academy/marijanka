def find_it(seq):
    a = {}
    for i in seq:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
            
    seq = []
    for i in a:
        if a[i] % 2:
            seq.append(i)

    return seq
