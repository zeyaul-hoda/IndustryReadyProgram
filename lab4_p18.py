#The distance between two cities in Km. is input through the keyboard. Write a
#program to convert and print the result in meters and centimetres.

from turtle import distance


distance = int (input("Enter the distance between two cities in kilometers: "))
mtr = (distance * 1000)
centimeter = (distance * 100000)
print("Distance between two cities in meters is: ",mtr)
print("Distance between two cities in centimeters is: ",centimeter)