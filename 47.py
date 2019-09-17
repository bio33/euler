def seive(limit):
    a = [True]*limit
    a[0] = a[1] = False

    for i,isPrime in enumerate(a):
        if isPrime:
            yield i
            for n in range(i*i,limit,i):
                a[n] = False


prime = seive(10**7)
primes = []
for i in prime:
    primes.append(i)

r = []
d = {}
for i in range(210,10**6):
    count = 0
    temp = i
    factors = []
    for p in primes:
        if temp == 1:
            break
        if temp % p == 0:
            pow = 1
            while temp % p == 0:
                temp = temp // p
                pow += 1
            factors.append(p**pow)
            count += 1
    if count == 4:
        r.append(i)
        d[i] = factors
    if len(r)> 4:
        if r[-1]- 1 == r[-2] and r[-2] - 1 == r[-3] and r[-3]-1 == r[-4]:
            print(r[-1])
            # print(d[r[-2]])
            # print(d[r[-3]])
            # print(d[r[-4]])
            break











