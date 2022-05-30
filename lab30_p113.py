# Write a program to compute the series
# 1 + 3 + 5 + 7 + 9 +........................ +n

n = int(input("Enter a number: "))
num = 0
print("Series till the enter number: ")
for i in range(1,n+1):
    if(i%2!=0):
        print(i, end=" ")
        num+=i