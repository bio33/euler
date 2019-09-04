def prime_seive(limit):
    primes = [True] * limit
    primes[0] = primes[1] = False
    for num,isPrime in enumerate(primes):
        if isPrime:
            yield num
            for i in range(num**2,limit,num):
                primes[i] = False



def isPan(num):
    limit = len(str(num))
    temp = []
    while num > 0:
        r = num % 10
        if r in temp or r > limit:
            return False
        else:
            temp.append(r)
            num //= 10
    return True



max_d = 8

limit = 10 ** max_d
get_prime = prime_seive(limit)

# pass all primes less than 4 digits
while next(get_prime) < 1000:
    next(get_prime)

for n in range(4, max_d):
    max_pan_n = 0
    prime = next(get_prime)
    while prime < 10 ** n:
        if isPan(prime):
            max_pan_n = prime if prime > max_pan_n else max_pan_n
        prime = next(get_prime)
    print(str(n) + " : " + str(max_pan_n))



