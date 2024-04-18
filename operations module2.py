import calculatoroperationmodule1
c=calculatoroperationmodule1.addition(10,20)
print("addition is:",c)

c=calculatoroperationmodule1.substraction(10,20)
print("substraction is:",c)

c=calculatoroperationmodule1.division(10,20)
print("division is:",c)


#From import

from calculatoroperationmodule1 import*
c=addition(50,20)
print("addition",c)

c=substraction(20,10)
print("substraction",c)



#FROM IMPORT
from calculatoroperationmodule1 import addition,substraction,division,multiplication
import calculatoroperationmodule1
c=addition(50,20)
print("addition",c)

c=substraction(20,10)
print("substraction",c)

c=division(50,20)
print("division",c)

c=calculatoroperationmodule1.multiplication(20,10)
print("multiplication",c)



