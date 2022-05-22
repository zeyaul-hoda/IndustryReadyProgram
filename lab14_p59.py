# Write a program to find the given number is prime or not.
#num = int(input("Enter a number: "))

from ast import Num


num = int(input("Enter number:"))
# prime numbers are greater than 1
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
   else:
    print(num,"is a prime number")