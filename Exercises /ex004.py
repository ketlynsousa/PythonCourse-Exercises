# Python Exercise 004 - Dissecting a Variable
# Write a program that reads something from the keyboard and displays on the screen its primitive type and all possible information about it.
from cmath import phase

phrase = input("Type anything: ")
print(f"The primitive type of this value is {type(phrase)}.")
print(f"Is there only spaces? {phrase.isspace()}.")
print(f"Is it a number? {phrase.isnumeric()}.")
print(f"Is it alphabetical? {phrase.isalpha()}.")
print(f"Is it alphanumeric? {phrase.isalnum()}.")
print(f"Is it in capital letters? {phrase.isupper()}.")
print(f"Is it in lowercase letters? {phrase.islower()}.")
print(f"Is it capitalized? {phrase.istitle()}.")
