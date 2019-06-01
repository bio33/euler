#Find the sum of all the multiples of 3 or 5 below 1000.
from functools import reduce
sum = []
for i in range(1,1000):
    if i%3 == 0 and i%5 == 0:
       sum.append(i)
    elif i%3 == 0:
        # prin
        sum.append(i)
    elif i%5 == 0:
        sum.append(i)


x = reduce(lambda x,y:x+y,sum)
print(x)

