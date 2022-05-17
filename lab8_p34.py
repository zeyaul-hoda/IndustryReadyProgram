# Write a program to read a 3-digit number and find whether the middle digit is
# numerically equal to the sum of the other two digits and prints an appropriate
# response.

from ast import Num


a = int(input("Enter a three digit number: "))
n = a % 10  #first number
a = int(a / 10) #third number
b = a % 10      # Second number
a = int(a / 10)
if b == (n + a):
    print("Middle digit is numerically equal to the sum of other two digits")
else:
    print("Middle digit is not numerically equal to the sum of other two digits")