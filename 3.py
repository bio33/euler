# find largest prime factor of n = 600851475143

import math
n = 600851475143

i = 2


while i < math.sqrt(n):
    while n%i == 0:
        n = n//i
        print(n)
    i+=1
    # print(i)

def isPrime(n):
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

