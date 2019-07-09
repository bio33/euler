# find lcm of 20 numbers
# using algo : a*b = lcm(a,b) * gcd (a,b)
from functools import reduce
def gcd(a,b):
    # think on this
    while b:
        a, b = b, a%b
    return a

#lcm = a*b/gcd(a,b)
def lcm (a,b):
    return a*b//gcd(a,b)

print(reduce(lcm,range(1,21)))
