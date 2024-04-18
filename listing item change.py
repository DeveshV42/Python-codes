x=["lenovo","hp","dell","asus"]
print("current list:",x)

#change the item in list
x[1:3]=["ipad","chromebook"]
print("updated list:",x)

#insert into list : updating list using insert method
l1=[1,2,3,4,5]
l2=['A','B','C','D','E']
l1.extend (l2)
print(l1)