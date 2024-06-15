'''23. Write a program that converts temperature from Celsius to Fahrenheit
and vice versa based on user input.'''
corf=int(input('''Celsius : 1 \nFahrenheit : 2 \nCelesius or Fahrenheit : '''))
if corf == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in fahrenheit : ",fahrenheit)
elif corf == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in celsius : ", celsius)
else:
    print("Please enter a value from  the menu")


