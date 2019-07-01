num = 2**1000

ans = 0
# print(num)
while num:
    ans += num % 10
    num = num // 10

# print(num)
print(ans)