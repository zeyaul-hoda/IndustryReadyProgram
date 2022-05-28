# Write a program to print the following triangle.
'''1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5 '''

num = int(input("Enter the number : "))
for i in range(0, num):
    n = 1
    for j in range(0, i + 1):
         print(n, end= " ")
         n = n + 1
    print()