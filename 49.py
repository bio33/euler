from itertools import permutations


def prime_seive(limit):
    primes = [True] * limit
    primes[0] = primes[1] = False
    for i,isPrime in enumerate(primes):
        if isPrime:
            yield i
            for x in range(i*i,limit,i):
                primes[x] = False


def find_permutations(num):
    l = []
    perms = permutations(str(num))
    for n in perms:
        # print(n)
        if n[-1]  not in '024658':
            x = int("".join(n))
            if x > 1000:
                l.append(x)
    return set(l)


limit = 100000
p = prime_seive(limit)
primes_required = []
while True:
    prime = next(p)
    x = len(str(prime))
    if x == 4:
        primes_required.append(prime)
    if x == 5:
        break


parsed = set()
for prime in primes_required:
        if prime not in parsed:
            parsed.add(prime)
            perms = find_permutations(prime)
            temp = []
            for num in perms:
                if num in primes_required:
                    parsed.add(num)
                    temp.append(num)
            if len(temp) >= 3:
                for i in range(0,len(temp)-2):
                    if temp[i+2] - temp[i+1] == temp[i+1] - temp[i]:
                        print(sorted(temp))

