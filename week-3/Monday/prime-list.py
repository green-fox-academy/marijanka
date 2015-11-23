for num in range(2,101):
    for n in range(2,num):
        if num % n == 0:
            break
        n +=1
    else:
        print(num)
