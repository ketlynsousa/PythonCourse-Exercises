# Python Exercise 014 - Temperature Converter
# Write a program that converts a temperature entered in degrees Celsius and converts it to degrees Fahrenheit.

print("=*" * 20)
print(f"{'CELSIUS TO FAHRENHEIT CONVERSION':^40}")
print("=*" * 20)
celsius = int(input("Enter degrees in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C converted is {fahrenheit:.0f}°F")
