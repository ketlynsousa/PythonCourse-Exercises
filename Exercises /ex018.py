# Python Exercise 018 - Sine, Cosine and Tangent
# Write a program that reads any angle and displays on the screen
# the value of the sine, cosine and tangent of that angle.
from math import sin, cos, tan, radians

print("Determining the sine, cosine and tangent of an angle.")
angle = float(input("Enter any angle from 0° to 360°: "))
print(f"Sine of {angle:.0f}°: {sin(radians(angle)):.2f}")
print(f"Cosine of {angle:.0f}°: {cos(radians(angle)):.2f}")
print(f"Tangent of {angle:.0f}°: {tan(radians(angle)):.2f}")
