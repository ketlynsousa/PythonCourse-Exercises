# Python Exercise 069 - Group Data Analysis
# Create a program that reads the age and gender of several people.
# For each registered person, the program should ask whether the user wants to continue or not. At the end, show:
# A) how many people are over 18 years old.
# B) how many men were registered.
# C) how many women are under 20 years old.
over_18_yo= 0
men_registered = 0
women_under_20 = 0

print('=' * 50)
print(f'{"REGISTERING SYSTEM":^50}')
print('=' * 50)

while True:
    #Age and gender registering
    age = int(input("Enter the age: "))
    gender = str(input("Enter the gender [F/M]: ")).strip().upper()
    while gender not in "FM":
        print("\033[1;31mInvalid option. Try again.\033[m")
        gender = str(input("Enter the gender [F/M]: ")).strip().upper()
    print("\033[32mREGISTERED SUCCESSFULLY.\033[m")
    print('=' * 50)

    if age > 18:
        over_18_yo += 1
    if gender == 'M':
        men_registered += 1
    if age < 20 and gender == 'F':
        women_under_20 += 1

    #Option to continue registering or stop the loop
    register = str(input("Do you wish to continue: [Y/N] ")).strip().upper()[0]
    while register not in ("Y", "N"):
        print("Invalid option. Try again.")
        register = str(input("Do you wish to continue: [Y/N] ")).strip().upper()[0]
    if register == 'N':
        break

print("\033[1;34mREGISTRATION COMPLETED.\033[m")
print('=' * 50)
print("ANALYSING REGISTRATION...\n")
print(f"You have registered {over_18_yo} people over 18 years old.")
print(f"You have registered {men_registered} men.")
print(f"You have registered {women_under_20} women under 20 years old.")
