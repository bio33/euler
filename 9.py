for a in range(0,1000//3):
    for b in range(0,1000//2):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print(a*b*c)