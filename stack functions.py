def push(num,n):
    num.append(n)
    return num

def pop(num):
        if isempty(num):
            print("stack is empty")
            return False
        else:
             num.pop()
             return num
def isempty(num):
        if not num:
             return True
        else:  
            return False

num=[]
push(num,2)
push(num,3)
push(num,4)
print(num)

#pop(num)
#pop(num)
#pop(num)
#print(num)