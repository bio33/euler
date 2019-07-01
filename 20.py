fac = 1

for i in range(1,101):
    fac = fac * i

fac_sum = 0
count = 0
while fac:
    count +=1
    fac_sum += fac % 10
    fac = fac//10

print(fac)
print(fac_sum)