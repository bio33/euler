# to-do 
max_p = 120
max_count = 3
for p in range(120,1001):
  count = 0
  for a in range(1, p):
    for b in range(a+1, p):
      c = p - a - b
      if a**2 + b**2 == c**2:
        # print(a,b,c)
        count +=1 
  if count > max_count :
    max_count = count
    max_p = p
  # print(max_p)

print(max_count)
print(max_p)
