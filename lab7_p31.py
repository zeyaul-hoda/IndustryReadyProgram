# Write a program to read ten numbers and print their sum by using ‘if’ statement.

a = (1,5,3,8,9,10,65,45,65,21)
i = 0
sum = 0
#For loop to perform addition of given numbers
for i in a:
    if i>0:
        sum += i;
print("Sum : ",sum)