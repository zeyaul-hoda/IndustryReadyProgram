# Write a program to compute the series.
# 1 + 3 + 6 + 10 +.……………………+ n

n = int(input("Enter a number: "))
num = 0
print("Series till the enter number: ")
for i in range(1,n+1):
    i=int(i * (i+1)/2)
    print(i,end=" ")
    num+=i