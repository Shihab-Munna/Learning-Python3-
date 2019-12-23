num = 1000
now_number = num
li = []
new_line =""
count =1

while count != num+5 :
    if count%5 == 0:
        li.append(str(now_number)+"\t")
    else :
        li.append(str(now_number)+"\t")

    if count%5 == 0:
        new_line ="".join(li)
        print(new_line)
        li = []
    else:
        pass
    now_number-=1
    count+=1
