#32
# in given conditions only 2digit x 3 digit = 4 digit numbers are fit for analysis.
# noob case 1digit x 4digit = 4digit

def check_pan(two,three,pro):
  
  temp = str(two) + str(three) + str(pro)
  # if "0" in temp:
  #   return False
  d = {str(k):0 for k in range(0,10)}
  for c in temp:
    d[c] += 1
  # if two == 39 and three == 186:
  #   print(d)
  for k,v in d.items():
    if k!= '0' and v != 1:
      return False
  return True
# 39 × 186 = 7254
# print(check_pan(40,186,7254))


final_sum = []

for two_digit in range(10,100):
  for three_digit in range(100,1000):
    val = two_digit * three_digit
    if len(str(val)) == 4:
      if check_pan(two_digit,three_digit,val):
        if val not in final_sum:
          final_sum.append(val)
          print("{0} * {1} = {2}".format(two_digit,three_digit,val))

for one_digit in range(1,10):
  for four_digit in range(1000,10000):
    val = one_digit * four_digit
    if len(str(val)) == 4:
      if check_pan(one_digit,four_digit,val):
        if val not in final_sum:
          final_sum.append(val)
          print("{0} * {1} = {2}".format(one_digit,four_digit,val))

print(sum(final_sum))
