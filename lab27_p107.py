# Write a program to print the following triangle.
'''  1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5'''

n = int(input("Enter the number of rows:"))
num = n + 1
for i in range(1, n + 1):
    for j in range(0, num):
        print(end= " ")
    for j in range(1, i + 1):
        print(j, end= " ")
    num = num - 1
    print("")