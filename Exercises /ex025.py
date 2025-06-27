# Python Exercise 025 - Searching for a string within another
# Make a program that reads a person's name and tells you if they have "Smith" in their name.

name = str(input("Enter your full name: ")).strip().title()
print(f"Is there Smith in the name? {'Smith' in name}.")
