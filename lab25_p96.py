# Write a program to print the following triangle.
'''1 2 3 4 5
     2 3 4 5
       3 4 5
         4 5
           5 '''

n = int(input("Enter the number of rows: "))
for i in range(0, n):
    num = 1
    for j in range(0,n):
        if(j < i):
            print(" ",end=" ")
        else:
            print(num, end=" ")
        num = num + 1
    print( " ")