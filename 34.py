# upper bound - > 2540161 (9!*7) reason being thats the maximum sum of factorials can go of each digit as 9999999

def memoize(f):
  memory = {}
  def helper(x):
    if x not in memory:
      memory[x] = f(x)
    return memory[x]
  return helper
@memoize
def fact(n):
  if n <= 1:
    return 1
  else:
    return n * fact(n-1)
d = {str(k): fact(k) for k in range(0,10)}
print(d)
s = 0
for i in range(10,2540161):
    temp = 0
    for c in str(i):
        temp += d[c]
        if temp > i:
            break
    if temp == i :
        s+=i

print(s)




