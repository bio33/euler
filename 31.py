def count_ways(s,m,n):
  if n < 0 :
    return 0
  if n == 0 :
    return 1
  if m <=0  and n >= 1:
    return 0
  
  return count_ways(s,m,n-s[m-1]) + count_ways(s,m-1,n)

def count(S, m, n): 
  
    # table[i] will be storing the number of solutions for 
    # value i. We need n+1 rows as the table is constructed 
    # in bottom up manner using the base case (n = 0) 
    # Initialize all table values as 0 
    table = [0 for k in range(n+1)] 
  
    # Base case (If given value is 0) 
    table[0] = 1
  
    # Pick all coins one by one and update the table[] values 
    # after the index greater than or equal to the value of the 
    # picked coin 
    for i in range(0,m): 
        for j in range(S[i],n+1): 
            table[j] += table[j-S[i]] 
  
    return table[n] 
x = print(count_ways([1,2,5,10,20,50,100,200],8,200))
