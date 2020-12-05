from calculator import *
from superCalculator import *

myCalc = SuperCalc()

n1 = input("Enter number 1: ")
n1 = int(n1)

n2 = input("Enter number 2: ")
n2 = int(n2)

print(addition(n1,n2))
myCalc.addition(1, 8)

# print(subtraction(n1,n2))
# print(multiplication(n1,n2))
# print(division(n1,n2))
# print(power(n1, n2))
