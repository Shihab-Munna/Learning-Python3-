li=[]

for i in range(1,101):
    if ( i % 3 == 0 and i % 5 != 0 ):
        li.append(i)

print(li)

for i in range (0,len(li)):
    print(li[i])