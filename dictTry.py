a = {'name' : 'Shihab Uddin Munna', 'phone' : '01711907520', 'email' : 'hmshiab891@gmail.com'}
print(a)
a['name'] ='Md Shihab Uddin Munna'
print(a)
del a['phone']
print(a)
b = a.copy()
print(b)
print(a.get('home','nai kichu'))
print('name' in a)
c = a.items()
print(c)
print(a.keys())
print(a.values())
