t = 2
p = 2
h = 2
tri = t * (t + 1)/2
penta = p * (3 * p - 1)/2
hexa = h * (2 * h - 1)
count = 0
while True:
    while tri < penta:
        tri = t * (t + 1)/2
        t += 1
    while penta < hexa:
        penta = p * (3 * p - 1) / 2
        p += 1
    while hexa < penta:
        hexa = h * (2 * h - 1)
        h += 1
    if hexa == penta and penta == tri:
        count += 1
        penta = p * (3 * p - 1) / 2
        if count == 2:
            print(tri)
            break
