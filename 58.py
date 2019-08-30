def isPrime(num):
    for i in range(2,int(num**.5)+1):
        if num % i == 0:
            return False
    return True
def corner_gen(n,i):
    return n**2 - i*n + i
n = 3
primes = 0


while True:
    sides = [corner_gen(n,i) for i in range(4)]
    for side in sides:
        if isPrime(side):
            primes += 1
    diagonals = 2*n - 1
    if primes/diagonals < .1 and n > 9:
        print(primes)
        print(diagonals)
        print(n)
        break

    n += 2
