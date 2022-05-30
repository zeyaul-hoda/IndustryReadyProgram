# Write a program to print the following triangle.
'''1 2 3 4 5
     1 2 3 4
       1 2 3
         1 2 
           1'''
n = int ( input ( "Enter the Number of Rows: " ))
for i in range ( 0, n+1 ):
    num = 1
    for j in range ( 0,n+1 ):
        if(j > i):
            print ( num, end= " ")
            num = num + 1
        else:
            print( " ", end= " ")
    print(" ")