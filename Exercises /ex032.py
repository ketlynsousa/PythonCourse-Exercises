# Python Exercise 032 - Leap Year
# Write a program that reads any year and shows if it is a leap year.
from datetime import date
print(f'Analysing if a YEAR is a leap year...')
year = int(input("Enter the year or 0 to analyse the current year: "))
if year == 0:
    year = date.today().year
if  year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"\033[4mThe year {year} is a leap year.\033[m")
else:
    print(f"\033[4mThe year {year} is not a leap year.\033[m")


