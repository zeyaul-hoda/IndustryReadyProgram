# Write a program to find the given number is palindrome or not.
from audioop import reverse
import numbers


number = int(input("Enter number: "))
temp = number
reverse = 0

while(number > 0):
    dig = number % 10
    reverse = reverse * 10 + dig
    number = number // 10

if temp == reverse:
    print("Number is palindrome")
else:
    print("Number is not Palindrome")