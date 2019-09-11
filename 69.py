def seive(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for n,isPrime in enumerate(a):
        if isPrime:
            yield n
            for i in range(n*n,limit,n):
                a[i] = False




temp = 1
s = seive(1000000)

primes = []

while temp < 10 ** 6:
    p = next(s)
    temp *= p
    primes.append(p)
    print(p,temp)
val = temp // primes[-1]

p = next(s)
while p < val:
    primes.append(p)
    p = next(s)
print(len(primes))
print(val/len(primes))
# print(temp)
# print(len(primes))
