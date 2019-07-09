import datetime


count = 0
for i in range(1901,2001):
    for x in range(1,13):
        temp = datetime.datetime(i , x, 1)
        if temp.strftime("%A") == "Sunday":
            print(temp.strftime("%c"))
            count += 1

print(count)