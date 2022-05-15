#The temperature of the city is input through the keyboard in Fahrenheit. Write
#a program to convert into Celsius

#fahrenheit = (celsius * 1.8) + 32 (Formula)
Fahrenheit  = float(input('Enter Fahrenheit  Value : '))

#calculates Fahrehheit to celcius 
Celcius = (Fahrenheit - 32) / 1.8
print(f'The Celcius of the entered Fahrenheit is : {Celcius}')