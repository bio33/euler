nums = ""
with open("8.txt") as data:
    l = data.readline().strip()
    while l:
        nums += l
        l = data.readline().strip()


window = 4
pro = 1
for i in range(window):
    pro = pro * int(nums[i])
mpro = 0
for i in range(window,len(nums)):
    if mpro < pro:
        mpro = pro
    if int(nums[i]) == 0:
        pro = 1
        i += 1
        for j in range(window):
            pro = pro * int(nums[i+j])
            i += 1
    else:
        try:
            pro = pro * int(nums[i]) // int(nums[i-window])
        except:
            i += 1 
print(mpro)