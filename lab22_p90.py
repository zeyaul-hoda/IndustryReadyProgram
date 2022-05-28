#Write a program to print the following triangle.
''' 1 1 1 1 1
    2 2 2 2
    3 3 3
    4 4
    5 '''

n = int(input( "Enter the Number of Rows: "))
for num in range(1,n+1):
    for i in range(num-n,1):
        print (num, end= " ")
    print ( " ")