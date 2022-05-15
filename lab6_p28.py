# Write a program to check whether the given year is leap year or not.

year = int(input("Enter year:"))
if year % 4 == 0:
    print("year is leap year")
else :
    print("Not leap year")