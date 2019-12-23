import random
li=[]
c=31
while len(li) is not 30:
    x = random.randint(1,101)
    if x not in li:
        li.append(x)
print(*li,sep=", ")