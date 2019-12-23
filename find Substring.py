def count_sub(str1, str2):
    return (sum([1 for i in range(0,len(str1)-len(str2)+1) if(str1[i:(len(str2)+i)] == str2)]))


string = "ABCDCDC"
sub = "CDC"

print(count_sub(string,sub))
