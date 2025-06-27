# Python Exercise 054 - Adulthood Group
# Create a program that reads the birth year of seven people.
# At the end, show how many people have not yet reached adulthood and how many are already adults.

from datetime import date
current_year = date.today().year
total_max = 0
total_min = 0
for person in range(1, 8):
    birthday_year = int(input(f"Enter the birthday year for the {person}ª person: "))
    age = current_year - birthday_year
    if age >= 21:
        total_max += 1
    else:
        total_min += 1
print(f"\nIn total, we have {total_max} people of legal age.")
print(f"And we also have {total_min} people under age.")
