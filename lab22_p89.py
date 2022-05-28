# Write a program to print the following triangle.
''' 1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1 '''

n = int(input("Enter the number of rows :"))
for i in range(0, n):
    num = 1
    for j in range(i-n, 0):
        print(num, end=' ')
        num = num + 1
    print()