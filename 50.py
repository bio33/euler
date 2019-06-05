#Which prime, below one-million, can be written as the sum of the most consecutive primes?
import time

import math
start = time.time()
def isPrime(x):
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

primes = []
for i in range(3,1000000,2):
    if isPrime(i):
        # print(i)
        primes.append(i)

print(time.time() - start)