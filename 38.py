def isPan(num):
  if '0' in str(num):
    return False
  t = {k:0 for k in range(1,10)}
  for i in str(num):
    t[int(i)] += 1
  for i in t:
    if t[i] != 1:
      return False
  return True

n = 10
t = 0
for num in range(1,5):
  for i in range(10**(num-1),10**(num)):
    temp = ""
    for z in range(1,n):
      temp += str(i * z)
      if len(temp) >= 9:
        break
    if len(temp) == 9:
      if isPan(temp):
        t = int(temp) if int(temp) > t else t

print(t)
