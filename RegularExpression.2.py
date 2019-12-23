import re
str = "purple alice@google.com, blah monkey bob@abc.com blah dishwasher"
temp = str.split(",")
for phrase in temp :
    result = re.match("([\w\.-]+)@([\w\.-]+)",phrase)
    print(result)
