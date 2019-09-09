d = {}
def sum_num(num):
    temp = 0
    while num > 0:
        temp += num % 10
        num //= 10
    return temp


for i in range(7,100):
    d[i] = []
    for y in range(2,10):
        if sum_num(i ** y) == i:
            d[i].append(i**y)
temp = []
for k,v in d.items():
    if len(v) > 0:
        for num in v:
            temp.append(num)

print(len(temp))
print(sorted(temp)[29])
