


def add(a, b, res = None):
    if res is None:
        res = []
    r = a + b
    res.append(r)
    print(res)
    return r

add(1,3)
add(2,3)
