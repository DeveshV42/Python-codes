#access value of dictionary
d1={1:"lenovo",2:"hp",3:"dell",4:"asus",'A':'b'}
print("current dict:",d1)

#access the value using key
x=d1[3]
print(x)

#access the value using get()
y=d1.get(2)
print(y)

#access the value using item
#z=d1.item()
#print(z)


#change the value
d1={1:"lenovo",2:"hp",3:"dell",4:"asus",'A':'b'}
d1[4]=("ipad")
print("updated dictionary:",d1)

#update dict using update method
d1.update({2:"mi"})
print("update dictionary:",d1)

#removing value from dict using pop()
d1.pop(2)
print("update dict:",d1)

#using pop item()
d1.popitem()
print("update dict:",d1)

#using del()
del d1[1]
print("update dict:",d1)

#usinng clear()
d1.clear()
print("update dict:",d1)

#access the only key from dictionary
d2={1:"lenovo",2:"hp",3:"dell",4:"asus",'A':'b'}
k=d2.keys()
print("keys:",d2)

#access the only value from dictionary
v=d2.values()
print("values:",v)


