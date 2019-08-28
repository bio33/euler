
def memoize(f):
  memory = {}
  def helper(x):
    if x not in memory:
      memory[x] = f(x)
    return memory[x]
  return helper

@memoize
def fact(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num * fact(num-1)
facts = {i:fact(i) for i in range(10)}

def fact_sum(num):
  temp = 0
  while num:
    temp += facts[num % 10]
    num //= 10
  return temp


parsed = {}
chain_count = 0
index = 69
while index < 1000000:
  if index not in parsed:
    chain = [index]
    temp = fact_sum(index)
    while temp not in chain:
      chain.append(temp)
      temp = fact_sum(temp)

    for i in range(len(chain)):
      parsed[chain[i]] = len(chain) - i

  index += 1

for k in parsed:
  if parsed[k] == 60:
    chain_count += 1

print(chain_count)
