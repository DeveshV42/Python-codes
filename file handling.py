#create a file
import os
os.getcwd()

os.chdir("D:\Personal docs")

f=open('file.txt','w')
f.write('i am Devesh')
f.write('\n i am from meerut')
print('Data written successfully')
f.close

#append a file
f=open('file.txt','a')
f.write('\n my house no. is 00')
print('data written successfully')
f.close

#Read the file
f=open('file.txt','r')
call=f.read()
print(call)
f.close()

#read the file in defining character
p=open('file.txt','r')
call=p.read(25)
print(call)
p.close()

#reades the line
g=open('file.txt','r')
call=g.readlines()
for lines in call:
    print(lines,end='')
    g.close


#create a file
#g=open('file1.txt','x')
#g.write('fix')
#print('fine')
#g.close()

#remove the file
os.remove('file1.txt')