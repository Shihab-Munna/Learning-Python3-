num=int(input('Enter a num to check :'))
check= int(input('One number to divide by:'))

if(num%4 == 0):
    print(num,' The number is a multiple of 4')
if(num%2 == 0):
    print(num,' is a Even Number.')
elif(num%2 != 0):
    print(num,' is a Odd Number')
if (num % check == 0):
    print(num,' is evenly divided by',check)
elif(num% check != 0):
    print(num,' is not evenly divided by',check)


