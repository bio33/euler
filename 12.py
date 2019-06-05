nums = ""
with open("12.txt") as f:
    number = f.readline().strip()
    while number:
        nums += number
        number = f.readline().strip()
answer = []
carry = 0
for k in range(49, -1, -1):
    temp_sum = 0
    for i in range(k, len(nums), 50):
        temp_sum = temp_sum + int(nums[i])
    if carry > 0:
        temp_sum += carry
    answer.append(temp_sum % 10)
    carry = temp_sum // 10
    
answer.append(carry)


print(list(reversed(answer))[:9])


