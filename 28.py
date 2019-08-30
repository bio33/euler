def corner_gen(n,i):
    return n**2 - i*n + i
n = 3
diagonal_sum = 1

while n < 1002:
    sides = [corner_gen(n,i) for i in range(4)]
    diagonal_sum += sum(sides)
    n += 2
print(diagonal_sum)
