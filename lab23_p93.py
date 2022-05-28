# Write a program to print the following triangle
''' 5
    5 4
    5 4 3
    5 4 3 2 '''

n = int(input( "Enter the number of rows: "))
for i in range(0, n):
    num = n
    for j in range(0, i+1):
        print(num, end = " ")
        num = num - 1
    print( " ")