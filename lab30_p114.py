# Write a program to compute the series.
# 1 + 4 + 9 + 16 +.…………………… + n

n = int(input("Enter a number: "))
num = 0
for i in range(1,n+1):
    i=i**2
    print(i, end=" ")
    num += i