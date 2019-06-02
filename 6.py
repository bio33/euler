#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import math
def sum_sqr(n):
    return math.pow(sum(range(1,n+1)),2)

def sqr_sum(n):
    return sum([i*i for i in range(1,n+1)])

n = 100
print(sqr_sum(n)-sum_sqr(n))