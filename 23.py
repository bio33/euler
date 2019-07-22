# non abundant sums

def sum_factors(num):
    factors = []
    for i in range(1,int(num//2)+1):
        if num % i == 0:
            factors.append(i)
    return sum(factors)

abundant_nums = []
for i in range(28112):
    x = sum_factors(i)
    if x > i:
        abundant_nums.append(i)

print("abundant sums complete")
# finding all possible # from abundant solutions
made_nums = [False] * 28124

for i in abundant_nums:
    for j in abundant_nums[1:]:
        num = i + j
        if i + j > 28123:
            break
        else:
            made_nums[num] = True
temp = 0

for i,v in enumerate(made_nums):
    if not v:
        temp += i
print(temp)



