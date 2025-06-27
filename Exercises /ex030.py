# Python Exercise 030 - Even or Odd?
# Create a program that reads an integer and displays on the screen whether it is EVEN or ODD.

print("Let's find out if the number is EVEN or ODD...")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is EVEN.")
else:
    print(f"The number {number} is ODD.")
