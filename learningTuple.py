n = int(input("How many elements ? :"))
a=()


for i in range (0,n):
    x = input("input %d :"%i)
    a = a+(x,)

print("Your Tuple is :",a)
print(a.count('1'))
print(len(a))
