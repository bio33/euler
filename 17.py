num_len = {
  1:len("one"),
  2:len("two"),
  3:len("three"),
  4:len("four"),
  5:len("five"),
  6:len("six"),
  7:len("seven"),
  8:len("eight"),
  9:len("nine"),
  10:len("ten"),
  11:len("eleven"),
  12:len("twelve"),
  13:len("thirteen"),
  14:len("fourteen"),
  15:len("fifteen"),
  16:len("sixteen"),
  17:len("seventeen"),
  18:len("eighteen"),
  19:len("nineteen"),
  20:len("twenty"),
  30:len("thirty"),
  40:len("forty"),
  50:len("fifty"),
  60:len("sixty"),
  70:len("seventy"),
  80:len("eighty"),
  90:len("ninety"),
  100:len("hundred"),
  "and":len("and"),
  1000:len("thousand")
}
temp_sum = 0
# sum 1-9
for i in range(1,10):
  temp_sum += num_len[i]

x = temp_sum

temp_sum = 0

# sum 10-19 
for i in range(10,20):
  temp_sum += num_len[i]

y = temp_sum

# sum 20-99
temp_sum = 0
for i in range(20,100,10):
  temp_sum += num_len[i] * 10 + x

z = temp_sum

#sum 1-99
k = x + y + z

# sum _00-_99
f = num_len[100] * 100 + num_len["and"] * 99 + k

# 1-1000
temp_sum = 0
for i in range(1,10):
  temp_sum += num_len[i] * 100 + f 

temp_sum += num_len[1000] + num_len[1] + k

print(temp_sum)









