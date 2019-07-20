super_dict = {}



def find_lcm(x,y):
  if x > y:
      z = x
  else:
      z = y

  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1

  return lcm

for x in range(1,7):
  temp = list(range(x*2,x*100+1,x))
  # print(temp)
  new_temp = []
  for key in super_dict.keys():
    limit = super_dict[key][-1]
    lcm = find_lcm(x,key)
    remove_nums = [i for i in temp if i <= limit and i % lcm == 0]
    print(len(remove_nums))
    new_temp.extend(remove_nums)
    # new_temp = filter_array(temp,lcm,super_dict[key][-1])
  if len(new_temp) == 0:
    super_dict[x] = list(temp)
  else:
    z = [a for a in temp if a not in new_temp]
    super_dict[x] = z

q = {k:len(v) for k,v in super_dict.items()}

# print(super_dict)
print(q)



#######################################

#29
import math
prime_list = []


  

total_count = 0
temp_count = 0
limit = 100
c = 99
d = {1: 99, 2: 50, 3: 50, 4: 41, 5: 51, 6: 37}
# d = {1: 4, 2: 4}
def isPrime(num):
  for x in range(2, int(num**.5)+1):
    if num % x == 0:
      return False
  return True

for x in range(2,limit + 1):
  temp_count = 0
  flag = True
  if isPrime(x):
    prime_list.append(x)
    temp_count += c
  else:
    for num in range(2,x):
      log = math.log(x,num)
      temp = str(log)
      # if log is a int 
      if temp[-1]=="0":
        w = d[log]
        temp_count += w
        print(x,temp_count)
        flag = False
        break 
    # if not a int execute this  
    if flag :
      temp_count += c
      print(x,c)
  total_count += temp_count
  print(total_count)


print(total_count)




