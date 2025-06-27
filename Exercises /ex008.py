# Python Exercise 008 - Measurement Converter
# Write a program that reads a value in meters and displays it converted to centimeters and millimeters.

meters = float(input("Enter the value in meters: "))
print(f"{meters} meters converted is {meters * 100:.0f} centimeters.")
print(f"{meters} meters converted is {meters * 1000:.0f} millimeters.")
