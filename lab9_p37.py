# Write a program to read a character and find out whether it is uppercase or
# lowercase.

char = input(" Enter Character:")
if char.isupper():
    print("Character is Upper case")
elif char.islower():
    print("Character is lower case")
else:
    print("Not a character")