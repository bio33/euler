temp = 0

def ispan(num):
    a = [True]*10
    while num > 0:
        r = num % 10
        a[r] = False
        num //= 10
    if any(a):
        return False
    else:
        return True

for d1 in range (1,10):
    for d2 in range(0,10):
        for d3 in range(0,10):
            for d4 in range(0, 10,2):
                for d5 in range(0, 10):
                    if (d3 + d4 + d5 )%3 == 0:
                        for d6 in [0,5]:
                            for d7 in range(0, 10):
                                if int(str(d5)+str(d6)+str(d7)) % 7 == 0:
                                    for d8 in range(0, 10):
                                        if int(str(d6) + str(d7) + str(d8)) % 11 == 0:
                                            for d9 in range(0, 10):
                                                if int(str(d7) + str(d8) + str(d9)) % 13 == 0:
                                                    for d10 in range(0, 10):
                                                        if int(str(d8) + str(d9) + str(d10)) % 17 == 0:
                                                            x = int(str(d1)+str(d2)+ str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9)+str(d10))
                                                            if ispan(x):
                                                                print(x)
                                                                temp += x
print(temp)
