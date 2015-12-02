def find_it(seq):
    find_it2 = []
    for i in seq:
        if i % 2 == 1:
            find_it2.append(i)
    find_it = set(find_it2)
    return find_it
