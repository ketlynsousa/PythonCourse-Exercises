# Python Exercise 027 - First and last name of a person
# Make a program that reads a person's full name, then displays the first and last name separately.
# EX: ANA MARIA DE SOUZA (First: Maria // Last: Souza)

name = str(input("Enter your full name: ")).strip().title()
print(f"The first name is {name.split()[0]}.")
print(f'The last name is name is {name.split()[-1]}.')

