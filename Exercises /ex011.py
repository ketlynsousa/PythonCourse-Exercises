# Python Exercise 011 - Painting a Wall
# Write a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it,
# knowing that each liter of paint paints an area of 2 square meters.

width = float(input("Type the wall width: "))
height = float(input("Type the wall height: "))
area = width * height
paint = area / 2
print(f"Your wall dimensions are {width}x{height} and its area is {area:.1f}m².")
print(f"To paint the wall completely you'll need {paint:.1f} liters of paint.")
