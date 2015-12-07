numbers_div = []
number = 10
i = 1
while i < number:
    if i % 3 == 0:
        numbers_div.append(i)
    elif i % 5== 0:
        numbers_div.append(i)
    i += 1
print(sum(numbers_div))
