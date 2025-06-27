# Python Exercise 038 - Comparing numbers
# Write a program that reads two integers and compares them, displaying a message on the screen:
# - The first value is greater
# - The second value is greater
# - There is no greater value, both are equal

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print("The first number is greater than the second number.")
elif num2 > num1:
    print("The second number is greater than the first number.")
else:
    print("The first and second numbers are equal.")
