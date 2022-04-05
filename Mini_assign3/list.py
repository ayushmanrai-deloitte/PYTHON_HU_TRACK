list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list_new=[]
for i in list1:
    for j in list2:
        temp = ""
        temp = temp+i+""+j
        list_new.append(temp)
print(list_new)