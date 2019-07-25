#46

def isPrime(num):
  for i in range(2,int(num**.5)+1):
    if num % i == 0:
      return False
  return True


primes = [2]

flag = True
num = 3
prime_flag = True
power_flag = True
while flag:
  if isPrime(num):
    primes.append(num)
  else:
    for prime in primes[::-1]:
      if (num - prime) % 2 == 0:
        val = str(((num - prime) // 2) ** .5)[-1]
        if val == '0':
          power_flag = True
        else:
          power_flag = False
      if power_flag and prime_flag :
        break
    if not (power_flag and prime_flag):
      print(num)
      flag = False
        

  num += 2
