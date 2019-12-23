li=[10, 5, 6, 10 , 6, 5 , 23, 22, 12, 3, 2, 33, 23, 443, 2]
my_list=[]
for i in li:
    if i not in my_list:
        my_list.append(i)

print(my_list)
