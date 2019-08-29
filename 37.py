def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False



import time
start = time.time()
limit = 10000000
count = 11
primes = []
a = primes_sieve2(limit)


for _ in range(4):
    primes.append(next(a))

res = 0

while count > 0:
    try:
        temp = next(a)
        primes.append(temp)
        num = str(temp)
        f = True
        if int(num[0]) % 2 != 8 or int(num[0]) % 2 != 4 or int(num[0]) % 2 != 6 :
            for i in range(1,len(num)):
                left = int(num[i:])
                right = int(num[:i])
                if left not in primes or right not in primes:
                    f = False
            if f:
                count -= 1
                res += temp
                print(num)
                print(count)
    except:
        print(count)
        break


print(res)

print(time.time()-start)
