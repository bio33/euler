import string
names = []
pos = {l:i for i,l in enumerate(string.ascii_lowercase, start = 1)}
with open("22.txt") as f:
    data = f.read().strip()
    names = data.split(",")
print(names)

names = sorted(names)

def word_score(name):
    name = name[1:-1]
    name = name.lower()
    score = 0
    for letter in name:
        score += pos[letter]
    if name == "colin":
        print(score)
    return score
total_score = 0
for i,name in enumerate(names,start = 1):
    if i == 938:
        print(i,name)
    total_score = total_score + word_score(name)*i
print(total_score)



