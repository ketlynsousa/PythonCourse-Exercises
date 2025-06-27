# Python Exercise 016 - Breaking a number
# Create a program that reads any Real number from the keyboard and displays its Integer portion on the screen.
# For instance, the integer of 6.127 is 6.
from math import trunc

real_num = float(input("Type a real number: "))
print(f"The integer part of {real_num} is {trunc(real_num)}.")
