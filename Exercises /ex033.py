# Python Exercise 033 - Largest and smallest values
# Write a program that reads three numbers and shows which is the largest and which is the smallest.
num1 = int(input("Type the first number: "))
num2 = int(input("Type the second number: "))
num3 = int(input("Type the third number: "))

max_number = max(num1, num2, num3)
min_number = min(num1, num2, num3)

print(f"The smallest number typed: {min_number}.")
print(f"The largest number typed: {max_number}.")
