#lychrel numbers


def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

lychrel_count = 0
for num in range(10 ,10001):
    count = 0
    temp = num
    while count < 50:
        x = str(temp)[::-1]
        temp += int(x)
        if isPalindrome(temp):
            count = 0
            break
        count += 1
    if count == 50:
        lychrel_count += 1

print(lychrel_count)

