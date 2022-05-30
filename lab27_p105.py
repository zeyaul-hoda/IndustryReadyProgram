# Write a program to print the following triangle.
'''      5
       4 4
     3 3 3
   2 2 2 2
 1 1 1 1 1 '''

n = int(input("Enter the number of rows: "))
num = n + 1
for i in range(1, n + 1):
    num = num - 1
    for j in range(0, n):
        if(j >= n - i):
            print(num, end= " ")
        else:
            print(" ", end= " ")
    print(" ")