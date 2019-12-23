for i in reversed(range (1,1001)):
    if (i%10 == 6 or i%10 == 1):
        print(i)
    elif (i != '1') :
        print(i,
              '\t', end="")