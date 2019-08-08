def memoize(f):
  memory = {}
  def helper(x):
    if x not in memory:
      # print("here")
      memory[x] = f(x)
    return memory[x]
  return helper
@memoize
def fib(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)
  
i = 1
z = [1]


while z[-1] < 10**999:
  z.append(fib(i))
  i+=1

print(i)
