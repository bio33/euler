def isPrime(num):
  num = num * -1 if num < 0 else num
  for i in range(2, int(num ** .5) + 1):
    if num % i == 0:
      return False
  return True

def find_val(n,a,b):
  return n**2 + a*n + b

max_n = -1
res = 1
for a in range(-1000,1001):
  for b in range(-1000,1001):
    n = 0
    val = find_val(n,a,b)
    while isPrime(val):
      n += 1
      val = find_val(n,a,b)
    
    if n > max_n:
      max_n = n
      res = a*b

print(res)
print(max_n)
