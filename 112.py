import time
def check_bouncy(num):
    f = 0
    temp = 0
    num = str(num)
    for i,c in enumerate(num[1:],1):
        v = int(num[i]) - int(num[i-1])
        if f == 0:
            if v > 0:
                f = 1
            elif v == 0:
                f = 0
            elif v < 0:
                f = -1
        else:
            if v > 0:
                temp = 1
            elif v == 0:
                temp = 0
            elif v < 0:
                temp = -1
            if temp * f < 0:
                return True
    return False



x = time.time()

bouncy = 0
index = 100
while True:
    if check_bouncy(index):
        bouncy += 1
    if 99 * index == bouncy * 100:
        break
    index += 1
print(index)
print(bouncy)
print("*"*20)
print(time.time() - x)

