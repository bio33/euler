total_count = 0
for base in range(1, 10):
    power = 1
    val = base ** power
    while power <= len(str(val)):
        if len(str(val)) == power:
            total_count += 1
        power += 1

print(total_count)
