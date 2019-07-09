import operator


chain_dict = {}


def compute_chain(num):
    if num in chain_dict.keys():
        return chain_dict[num]

    num = num//2 if num % 2 == 0 else 3*num + 1
    if num == 1:
        return 0
    else:
        chain_dict[num] = 1 + compute_chain(num)
        return chain_dict[num]

for i in range(2,1000000):
    chain_dict[i] = 1 + compute_chain(i)

max_num = max(chain_dict.items(), key = operator.itemgetter(1))
print(max_num)
