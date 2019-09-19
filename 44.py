def ispenta(num):
    temp = ((24 * num + 1) ** .5 + 1) / 6
    if int(((24 * num + 1) ** .5 + 1) / 6) == temp:
        return True
    else:
        return False


for i in range(2, 10 ** 6):
    p = i * (3 * i - 1) / 2
    for j in range(i - 1, 0, -1):
        q = j * (3 * j - 1) / 2
        if ispenta(p + q) and ispenta(p - q):
            print(p - q)
            break
