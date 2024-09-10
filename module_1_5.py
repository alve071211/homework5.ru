immutable_var=(12,[15,8],"школа",True)
print(immutable_var)
#immutable_var[0]=3
#print(immutable_var) #не дает изменить элемент кортежа потому что это последовательность имён
mutable_list=["pen","pencil","book"]
mutable_list[1]="bag"
print(mutable_list)