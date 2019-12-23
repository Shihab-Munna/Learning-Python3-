str = input ('Enter a Word :')
if str.lower() == str[::-1].lower():
    print("%s is a Palindrome word "%str)
else :
    print ("%s is not a palindrome word "%str)
