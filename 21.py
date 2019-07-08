# def find all divisors

def get_divisors(num):
  divs = []
  for i in range(1,num//2+1):
    if num%i == 0 :
      divs.append(i)
  return sum(divs)


def main():
  num_list = {}
  temp_sum = 0
  for i in range(2,10000):
    num_list[i] = get_divisors(i)
  
  for k,v in num_list.items():
    if v in num_list.keys() and k == num_list[v] and k!=v  :
      temp_sum += k
      print(k,v)
  print(temp_sum)
  # print(num_list)

main()


