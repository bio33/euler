# find largest palindrome from 3 digigts



# check pailindrome

def isPalindrome(n):
    string_n = str(n)
    if len(string_n) % 2 == 0:
        half = string_n[:len(string_n)//2]
        second_half = string_n[len(string_n)//2:]
    else:
        half = string_n[:len(string_n) // 2]
        second_half = string_n[len(string_n) // 2 + 1:]


    if half == second_half[::-1]:
        return True
    return False
palindromes = []
for i in range(999,900,-1):
    for j in range(999,900,-1):
        num = i*j
        if isPalindrome(num):
            palindromes.append(num)
print(max(palindromes))
