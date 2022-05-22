# Write a program to display the multiplication table for a given number

from itertools import count


number = int(input ("Enter the number: "))      
# We are using "for loop" to iterate the multiplication 10 times       
print ("The Multiplication Table of: ", number)    
for i in range(1, 11):      
   print (number, "*", i, '=', number * i)
   