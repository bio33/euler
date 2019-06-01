#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


from functools import lru_cache

@lru_cache(maxsize=50)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib (n-2)

nums = [fib(i) for i in range(50)]

nums = filter(lambda x: x < 4000000, nums)
print(list(nums))
print(sum([x for x in nums if x%2 == 0]))