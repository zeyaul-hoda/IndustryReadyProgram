# Write a program to find the second smallest number and its position among
# the given ‘n’ numbers.

from turtle import position


list = [10, 20, 4, 45, 99]
list.sort()
print("Second largest element is:", list[-2]) # I found second largest number
print(list.index(45))