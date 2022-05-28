# Write a program to print the following triangle
''' 5 4 3 2 1
    5 4 3 2
    5 4 3
    5 4
    5 '''

n = int(input( "Enter the number of rows: "))
for i in range(0,n+1):
    for j in range(n,i,-1):
        print(j,'',end='')
    print(' ')