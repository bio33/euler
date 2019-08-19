p = {i:i**5 for i in range(0,10)}
s= 0
for num in range(2,10**7):
    digits = []
    t = num
    while num:
        digits.append(p[num%10])
        num = num//10
        # print (num)
    if sum(digits) == t:
        print(t)
        s += t

    
print(s)
