a = {1, 2, 3, 4, 5}
b = {5 , 6, 7, 8}
li1 =list(a)
li2 =list(b)
union = set(li1+li2)
inter = [x for x in a if x in b]

print("A =",*a,sep=" ")
print("B =",*b,sep=" ")
print("Union =",*union,sep=" ")
print("Intersection =",*inter,sep=" ")



