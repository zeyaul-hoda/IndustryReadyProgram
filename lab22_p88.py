# Write a program to print the following triangle.
''' 1
    1 1
    1 2 1
    1 2 3 1
    1 2 3 4 1 '''

from ast import Num


num = int(input("Enter the number of rows: "))
for i in range(0 , num):
    for j in range(1, i + 1):
        print(j, end= ' ')
    print(1)
    print("")