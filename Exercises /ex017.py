# Python Exercise 017 - Legs and Hypotenuse
# Create a program that can determine the lengths of a right triangle's adjacent and opposing legs.
# Determine the hypotenuse's length and display it.
from math import hypot

print("FINDING THE HYPOTENUSE OF A RIGHT TRIANGLE")
opposite_side = float(input("Enter the opposite side: "))
adjacent_side = float(input("Enter the adjacent side: "))
hypotenuse = hypot(opposite_side, adjacent_side)
print(f"The hypotenuse length is {hypotenuse:.2f}.")
