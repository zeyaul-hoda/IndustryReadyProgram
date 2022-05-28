# Write a program to print the following triangle.
''' 1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5  '''

n = int(input("Enter the number of rows: "))
for num in range(1, n + 1):
    for i in range(0, num):
        print(num, end= ' ')
    print()