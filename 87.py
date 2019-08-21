def isPrime(num):
  num = num * -1 if num < 0 else num
  for i in range(2, int(num ** .5) + 1):
    if num % i == 0:
      return False
  return True

primes = [2]
# upper limit for primes would be √50000000 
for i in range(3,7071,2):
  if isPrime(i):
    primes.append(i)


limit = 50000000
nums = []
for pow2 in primes:
  x = pow2**2
  if x < limit:
    for pow3 in primes:
      y = pow3 ** 3
      if y < limit:
        for pow4 in primes:
          z = pow4 ** 4
          if z < limit :
            val = x + y + z
            if val <= limit:
              nums.append(val)

print(len(set(nums)))
