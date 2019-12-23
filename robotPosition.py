x=int (input("Enter Current Point :"))
y=int (input())

while(1):
    c=input('Enter Command :')
    if (c == 's' or c =='S'):
        break
    else:
        if (c == 'U' or c== 'u'):
            x-=1
        elif(c == 'd' or c == 'D'):
            x+=1
        elif(c =='r' or c =='R'):
            y+=1
        elif(c== 'l' or c=='L'):
            y-=1
        else:
            print('Wrong Command!!!')

print('Current Position Of Robot :',x,y)


