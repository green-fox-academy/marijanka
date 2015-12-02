def divisors_find(integer):
    if integer == 1:
        return(1)
    else:
        divisors_list = []
        for n in range(2, integer):
            if integer % n == 0:
                divisors_list.append(n)
        return divisors_list

def divisors(integer):
    div_list = divisors_find(integer)
    if len(div_list) > 0:
        return div_list
    else:
        return "{} is prime".format(integer)

# def divisors(num):
#     l = [a for a in range(2,num) if num%a == 0]
#     if len(l) == 0:
#         return str(num) + " is prime"
#     return l
