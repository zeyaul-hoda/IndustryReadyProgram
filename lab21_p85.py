# Write a program to print the Floyd’s triangle.
'''1
   2 3
   4 5 6
   7 8 9 10'''

from pickle import APPEND


num = int(input("Enter the number of rows :"))
n = 1
print( "Floyd Triangle" )
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(n, end =' ')
        n = n + 1
    print()
