#greater of two number

print('enter two numbers')
x=input('enter first number:')
y=input('enter second number')
try:
    if int(x) > int(y):
     print(x+'is greater')
    else:
     print(y+' ','is greater')

except ValueError:
    print('you did not entered numeric value')


