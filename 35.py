from itertools import permutations
import math
def isPrime(num):
  for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
      return False
  return True

def find_numbers(num):
  perms = permutations(str(num),len(str(num)))
  nums = map("".join, perms)
  return list(map(int , list(nums)))

def find_nums(num):
  nums = []
  l = len(str(num))
  for i in range(l):
    ld = num % 10
    num = num // 10
    num = ld * 10 ** (l-1) + num
    nums.append(num)
#  print(nums)
  return nums
  
  def check_prime(num_list):
  for num in num_list:
    if not isPrime(num):
      return False

  return True
count = 1
temp = {}
for i in range(3,1000000,2):
  num_list = find_nums(i)
  if check_prime(num_list):
    print(i)
    count +=1

print(count)

