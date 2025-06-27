# Python Exercise 022 - Text Analyzer
# Create a program that reads a person's full name and displays:
# - The name with all upper and lower case letters.
# - How many letters in total (without considering spaces).
# - How many letters are in the first name.

name = str(input("Type your full name: ")).strip()
print("Analysing the name...")
print(f"Full name in upper case letters: {name.upper()}.")
print(f"Full name in lower case letters: {name.lower()}.")
print(f'Your full name has a total of {len(name.replace(' ', ''))} letters.')
print(f"Your first name {name.split()[0]} has {len(name.split()[0])} letters.")
