# Write a program to print the following triangle.
'''       1
        2 3 2
      3 4 5 4 3
    4 5 6 7 6 5 4
  5 6 7 8 9 8 7 6 5 '''

n=int(input("Enter the number of rows: "));
num = n
a = 1
for i in range(1,n+1):
    for j in range(1,num):
        print(" ", end=" ")
    for j in range(1,a+1):
        print(i, end=" ")
        if (j<=a/2 ):
            i=i+1
        else:
            i=i-1
    a=a+2
    num=num-1
    print( " ")