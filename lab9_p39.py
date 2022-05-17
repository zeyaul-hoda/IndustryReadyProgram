# Write a program to check whether the given input is digit or lowercase
#character or uppercase character or a special character.

a = input("Enter input; ")
if a >= '0' and a <= '9':
    print("digit")
elif a.isupper():
    print("Upper character")
elif a.islower():
    print("Lower char")
else :
    print("Is Special character")