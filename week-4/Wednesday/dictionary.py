students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

def candies(list):
    candies_count = 0
    for i in list:
        if i['candies'] > 4:
            candies_count += 1
    return candies_count

print(candies(students))

def is_rich(kid):
    return kid['candies'] > 4

def filter_rich(peeps):
    return len(list(filter(is_rich.peeps)))

print(filter_rich(students))

def rich_kids_in_one_line_bro(fellas):
    return len(list(filter(lambda x: x['candies'] > 4, fellas)))

print(rich_kids_in_one_line_bro(students))
