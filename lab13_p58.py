# Write a program to print the numbers which are divisible by both 3 and 7 from
#1 to 100.

from ast import Num


print("Number which is divisible by 3 and 7 :") 
for i in range(1,100):
    if (i % 3 == 0 and i % 7 == 0):
        print(i)