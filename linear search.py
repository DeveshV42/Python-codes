def linearsearch(num,key):
    for i in range(len(num)):
        if key==num[i]:
             return True
    return False

num=[2,3,6,2,4,9,7,3,3,6,1,0]
key=8

if linearsearch(num,key):
    print(key,"is found in the list")
else:
    print(key,"is not found in the list")

    