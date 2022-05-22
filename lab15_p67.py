# Write a program to print the reverse of a given number

from math import remainder


number = int(input("Enter number : "))
reverse = 0
while (number > 0):
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number // 10
    
print("Reverse number = ", reverse)