t = int(input())
for i in range (0,t):
    n = int (input())

    for j in range (0,n):
        for k in range (0,n):
            print("*",end="")
        print()
    if i == t-1:
        break
    else:
        print()