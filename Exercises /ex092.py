# Python Exercise 092 - Python Worker Registration
# Create a program that reads name, year of birth and working card ID and register it (with age) in a dictionary.
# If WC ID  is different from zero, the dictionary will also receive the year of hiring and salary.
# Calculate and add, besides the age, how old the person will retire.
from datetime import date
register = dict()
register['Name'] = str(input("Enter the name: ")).strip().title()
birth_year = int(input("Enter the year of birth: "))
register['Age'] = date.today().year - birth_year
register['WC ID'] = int(input("Enter the Nº for WC ID or (0 if N/A): "))

if register['WC ID'] == 0:
    print("=*" * 20)
    print("REGISTER".center(40))
    print("=*" * 20)
    for key, value in register.items():
        print(f"- {key}: {value}".center(40))
else:
    register['Year of hiring'] = int(input("Enter the hiring year: "))
    register['Salary'] = float(input("Enter the salary: $"))
    register['Retirement age'] = (register['Year of hiring'] + 35) - birth_year
    print("=*" * 20)
    print("REGISTER".center(40))
    print("=*" * 20)
    for key, value in register.items():
        print(f"- {key}: {value}".center(40))
