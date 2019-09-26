


def larges_perm(num):
    x = int("".join(sorted(str(num),reverse=True)))
    return x


cubes = [0]

def main_2():
    for i in range(1,10**4):
        cubes.append(i**3)
    d = {}
    for i,cube in enumerate(cubes):
        t = larges_perm(cube)
        if t not in d:
            d[t] = [i,1]
        else:
            d[t][1] += 1
            if d[t][1] >= 3:
                print(d[t])
            if d[t][1] == 5:
                print(d[t])
                print(cubes[5027])
                exit(1)



main_2()


