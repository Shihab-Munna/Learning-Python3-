while (True):
    print("Welcome to Simple Calculator")
    print("To Quiet Press : Q ")
    print("To Add two number Press : A")
    print("To subtract two numbers Press: S")
    print("To multiply two numbers Press : M")
    print("To divide two numbers Press : D")
    user=input("Enter Your Choice:")

    if (user == 'Q' or user == 'q'):
        print("Thanks For Using")
        break
    elif(user == 'a' or user == 'A'):
        a=int(input("Enter the 1st Number:"))
        b=int (input(("Enter the 2nd Number:")))
        print("The Sum = ",a+b)

    elif (user == 's' or user =='S'):
        a = int(input("Enter the 1st Number:"))
        b = int(input(("Enter the 2nd Number:")))
        print("The Result = ", a - b)

    elif (user == 'm' or user =='M'):
        a = int(input("Enter the 1st Number:"))
        b = int(input(("Enter the 2nd Number:")))
        print("The Result = ", a * b)


    elif (user == 'D' or user =='d'):
        a = int(input("Enter the 1st Number:"))
        b = int(input(("Enter the 2nd Number:")))
        print("The Result = ", a / b)

    else :
        print("Wrong Input !!\n")
