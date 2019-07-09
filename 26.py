# find recurring cycle of decimal numbers

def find_cycle(num):
    pass

max_len = 0
for num in range(1,1000):
    cycle_len = find_cycle(num)
    if cycle_len > max_len:
        max_len = cycle_len
        winner_num = num

print(winner_num + ": " + 1/winner_num)