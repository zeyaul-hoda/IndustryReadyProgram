#  Two numbers are input into two locations ‘a’ and ‘b’. Write a program to
# interchange the contents of ‘a’ and ‘b’ without using temporary variables.

a = int(input("Enter value of first variable: "))
b = int(input("Enter value of second variable: "))
#prints a and b before swap
print("Before swap the values of a and b are", a, b)
#After swap  
a ,b = b , a
print("Before swap the values of a and b are", a,b) #no temperory variable used direct method used to swap