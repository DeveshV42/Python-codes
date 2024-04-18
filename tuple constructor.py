t3=(("lenovo","hp","dell","asus"))
print(t3)


#add item after converting tuple into list

t4=("lenovo","hp","dell")
print("current tuple:",t4)

print(type(t4))

#convert tuple into list
x=list(t4)
print(x)

print(type(t4))

#add item into list
x[1]="asus"
print("updated list:",x)

#convert list into tuple again
y=tuple(x)
print("updated tuple:",y)