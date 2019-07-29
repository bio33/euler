#42
import string

d = {c:v for v,c in enumerate(string.ascii_lowercase,1)}
def triangle(n):
  return n*(n+1)//2


def word_sum(word):
  s = 0
  for c in word:
    s += d[c]
  return s


x = triangle(10)
count = 0

tri_nums = []
tri_nums.append(triangle(1))
n = 2
with open("data.txt","r") as f :
  l  = f.readline()
  while l:
    words = l.lower().split(",")
    for word in words:
      word = word[1:-1]
      word_score = word_sum(word)
      while word_score > tri_nums[-1]:
        n+=1
        tri_nums.append(triangle(n))
      if word_score in tri_nums:
        print(word)
        count += 1
    l = f.readline()
  print(count)




