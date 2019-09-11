with open("59.txt","r") as f:
    data = f.read()
    temp = data.split(",")
    print(len(temp))
    s = 1
    limit = 12
    sample = list(map(int,temp[:limit]))

    for k1 in range(97,123):
        for k2 in range(97,123):
            for k3 in range(97,123):
                message = []
                for i in range(0,limit,3):
                    t1,t2,t3 = sample[i:i+3]
                    message.append(t1 ^ k1)
                    message.append(t2 ^ k2)
                    message.append(t3 ^ k3)
                flag = True
                for char in message:
                    if not ((char >=65 and char <= 91) or (char >=97 and char <=122) or char == 32):
                        flag = False
                if flag:
                    message = [chr(i) for i in message]
                    print("".join(message) + " " + chr(k1) + chr(k2) + chr(k3))

    key = [ord('e'),ord('x'),ord('p')]
    res = 0
    for i in range(0,len(temp),3):
        for k in range(3):
            res += int(temp[i+k]) ^ key[k]
    print(res)









