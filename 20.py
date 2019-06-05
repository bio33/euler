fac = 1

for i in range(1,101):
    fac = fac * i

fac_sum = 0

while fac:
    fac_sum += fac % 10
    fac = fac//10


print(fac)
print(fac_sum)