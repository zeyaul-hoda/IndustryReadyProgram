# Write a program to print all prime numbers from 1 to 99.

from ast import Num


print("Prime numbers between 1 to 99")
for n in range(1,99):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                break
        else:
            print(n)
