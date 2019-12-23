n=int(input('Enter The Number Of elements :'))
li=[]

for i in range(0,n):
    ele=int(input())

    li.append(ele)
print(li)

for i in range(0,n):
    if(li[i] % 2 == 0 ):
        print(li[i],"Is a Even Number")

    else :
        print(li[i],"is an Odd Number")

