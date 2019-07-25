# steps
# find all the primes below 1 mill
# find the longest string which adds up to a prime

limit = 1000000
def isPrime(num):
  for i in range(2,int(num**.5)+1):
    if num % i == 0:
      return False
  return True

primes = [2]
for i in range(3,limit,2):
  if isPrime(i):
    primes.append(i)

# find the longest sequence which adds to primes
ps  = 0
ps_len = 0
for i in range(len(primes)):
  temp = 0
  l = []
  for j in range(i,len(primes)):
    if temp < limit:
      temp += primes[j]
      l.append(primes[j])
      if isPrime(temp) and len(l) > ps_len:
        print(l)
        ps = temp
        ps_len = len(l)
    else:
      break

print(ps)
