from functools import reduce
with open("8.txt","r") as f:
  temp = ""
  x = f.readline().strip()
  while x:
    temp += x
    x = f.readline().strip()
  max_pro = 1
  for i in range(0,987):
    t = [int(x) for x in temp[i:i+13]]
    print(t)
    pro_t = reduce(lambda x,y:x*y, t)
    if pro_t > max_pro:
      max_pro = pro_t
  print(max_pro)
    
