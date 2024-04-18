print('hello')
try:
    c=int(input("enter value"))+4
    #c=b+4
except ValueError:
    print('error! you cant enter string')
except NameError:
        print("error! variable not defined")
