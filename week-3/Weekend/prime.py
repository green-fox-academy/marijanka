function getPrimes(start, finish) {
    prime_list =[]
    for x in range(start, finish+1):
        isPrime=True
        for y in range(2,int(x**0.5)+1) :
            if x % y == 0:
                isPrime = False
                break
        if isPrime:
            prime_List.append(x)
    return(prime_list)
}
