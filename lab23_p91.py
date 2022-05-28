# Write a program to print the following triangle.
''' 5 5 5 5 5
    4 4 4 4
    3 3 3
    2 2
    1 '''

n = int(input( "Enter the Number of Rows: "))
i = n
while(i >= 1):
    for j in range(1, i + 1):
        print(i, end = ' ')
    i = i - 1
    print("")