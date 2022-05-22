  # Write a program to find the factorial of the given number.

from math import factorial


numb = int(input("Enter Number: "))
i = 1
fact = 1
while 1 <= numb:
    fact *= i
    i += 1
print("factorial of " ,numb, fact)