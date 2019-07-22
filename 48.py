
total_sum = 0

for x in range(1,1000):
    total_sum += x**x

print(total_sum % 10**10)