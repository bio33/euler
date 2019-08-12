# a^b = x
# log(a)(x)=b
# change base for each log -> log(e)(x)/log(e)log(a) = b
# log(e)(x) = b * log(e)(a)
# x - > b * log(e)(a)   [Since every number is of the same power of e , we can ignore it]



import math

temp = 0
i = -1
with open("99.txt",'r') as f:
  data = f.readlines()
  for index,line in enumerate(data,1):
    num,power = list(map(int,line.split(",")))
    t = power * math.log(num)
    if t > temp:
      temp = t
      i = index
  
  print(i)
  
