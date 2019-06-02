# finding nth prime number
import math
n = 10001

count = 1

def isPrime(x):
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

num = 3

while count < n:
    if num % 2 != 0:
        if isPrime(num):
            count += 1
    num += 1
print(num)