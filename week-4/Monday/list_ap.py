ag2 = ['rep', 'macsk', 'cic', 'alm', 'Ann', 'kacs']

def something(string_a):
    return string_a + 'a'

for i in range(len(ag2)):
    ag2[i] = something(ag2[i])

print(ag2)
