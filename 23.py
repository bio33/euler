# abundant sum


def sum_factors(num):
  fact = []
  for i in range(1,num//2 + 1) :
      if num % i == 0:
          fact.append(i)
  return sum(fact)


def check_num(num):  
  if sum_factors(num) > num:
      return True
  return False

nums = []
for i in range(4,28123):
  if check_num(i):
      nums.append(i)

# print(nums)
print(len(nums))

temp = [0]*28124
for num1 in nums:
  for num2 in nums:
    i = num1 + num2
    if i > 28123 :
      break
    else:
      temp[i] = 1

a = 0
for i,v in enumerate(temp):
  if v != 1:
    print(i)
    a += i

print(a)
