# Write a program to print the following triangle.
'''5 5 5 5 5
     4 4 4 4
       3 3 3
         2 2
           1 '''

n = int(input("Enter the Number of Rows: "))
b = n+1
for num in range(1,n+1):
    b=b-1
    for i in range(1,n+1):
        if(i < num):
            print ( " ", end=" " )
        else:
            print(b, end=" ")
    print(" ")