# A Company insures its drivers in the following cases.
''' 1. If the driver is married.
2. If the driver is unmarried, male and above 30 years of age.
3. if the driver is unmarried, female and above 25 years of age.
In all other cases, the driver is not insured. If the marital status, sex, age of the
driver are the inputs, write a program to determine whether the driver is insured
or not. '''

marital_status = ("Enter marital status: ")
gender = input("Enter driver gender(male/female):")
age = input( "Enter driver age:" )

if marital_status == 'married':
    print("Driver is insured")
elif marital_status == 'unmarried' and 'male' > 30:
    print("Driver is insured")
elif marital_status == 'unmarried' and 'female' > 25:
    print("Driver is insured")
else:
    print("Driver is not insured")