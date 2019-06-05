import math

def isPrime(x):
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def mySolution():
    init_sum = 17


    for i in range(9,2000000,2):
        if isPrime(i):
            init_sum += i

    print(init_sum)

def Eratosthenes():
    num_list = list(range(3,2000000,2))
    count = 0
    while num_list[count]**2 <= num_list[-1]:
        prime = num_list[count]
        num_list = list(filter(lambda x : x % prime != 0, num_list))
        num_list.insert(count,prime)
        count += 1
    print(sum(num_list)+2)

Eratosthenes()