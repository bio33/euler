n = 23123568
def find_divisors(n):
    exp = {}
    d = 2
    if n % d == 0:
        exp[d] = 0
        while n%d == 0:
            n = n // d
            exp[d] += 1
    d = 3
    while n > 2:
        if n % d == 0:
            exp[d] = 0
            while n % d == 0:
                n = n // d
                exp[d] += 1
        d += 2




    # print(exp)
    divs = 1
    for k,v in exp.items():
        divs = (v+1) * divs
    # print(divs)
    return divs
k = 10
while True:
    a = sum(range(1,k+1))
    div = find_divisors(a)
    if div > 500:
        print(a)
        break
    k += 1
