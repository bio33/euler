def find_sum(n):
  temp = 0
  while n > 0:
    d = n % 10
    n = n//10
    temp += d
  return temp

z = 0
for a in range(2,100):
  for b in range(2,100):
    v = find_sum(a**b)
    z = v if v > z else z

print(z)
