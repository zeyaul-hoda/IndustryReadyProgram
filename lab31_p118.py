# Write a program to compute the series.
# 1! + 2! + 3! + 4! +.………….……...+ n

n = int(input("Enter a number: "))
num = 0
fact=1
print("Series till the enter number: ")
for i in range(1,n+1):
    fact*=i
    i+=1
    print(fact, end=" ")
    num+=fact