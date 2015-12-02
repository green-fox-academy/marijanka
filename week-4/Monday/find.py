students = [
    {'name': 'tibi', 'age': '8'},
    {'name': 'adorjan', 'age': '9'},
    {'name': 'agoston', 'age': '6'},
    {'name': 'aurel', 'age': '7'},
    {'name': 'dezso', 'age': '12'}
]

students_at_least_8 = []

for i in students:
    if int(i['age']) >= 8:
        students_at_least_8.append(i['name'])
print(students_at_least_8)

students_ages_starting_with_A = []

for i in students:
    if i['name'][0] == 'a':
        students_ages_starting_with_A.append(i['name'])
print(students_ages_starting_with_A)
