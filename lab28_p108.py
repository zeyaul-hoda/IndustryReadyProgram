# Write a program to print the following triangle.
''' 5 5 5 5 5
     4 4 4 4
      3 3 3
       2 2
        1 '''

n = int(input("Enter the number of rows: "))
b = n+1
for i in range(n+1,1,-1):
    b = b-1
    for j in range(0, n-i+1):
        print(end=" ")
    for j in range(0, i-1,1):
        print(b, end=" " )
    print(" ")