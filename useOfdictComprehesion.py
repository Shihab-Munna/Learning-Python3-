my_dict = {'name':'Munna', 'age':'21', 'phone':'017'}

new_dict = {key:value for value,key in my_dict.items()}
print(new_dict)
dict_2 ={value:key for key,value in new_dict.items()}
print(dict_2)