# Python Exercise 039 - Military Enlistment
# Write a program that reads the year of birth of a young man and informs, according to his age, whether he will still enlist
# for military service, if it is the year to enlist or if it is past the enlistment period.
# Your program should also show the time left or the time that has passed.
from datetime import date

birthday_year = int(input("Enter your year of birth: "))
current_year = date.today().year
age = current_year - birthday_year

if age == 18:
    print(f"The age to enlist is 18. You are in the year for your enlistment period.")
elif age < 18:
    enlistment = 18 - age
    enlistment_year = current_year + enlistment
    print(f"The minimum age for enlistment is 18. You are not currently in the enlistment period."
          f"\nYou have {enlistment} years remaining till you enlist. Your enlistment year is {enlistment_year}.")
else:
    enlistment = age - 18
    enlistment_year = enlistment - current_year
    print(f"The enlistment age is 18. You have already passed {enlistment} years of service period."
          f"\n{enlistment_year} was your enlistment year.")
