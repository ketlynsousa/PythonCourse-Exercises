# Python Exercise 057 - Data Validation
# Make a program that reads a person's gender, but only accept the values 'M' or 'F'.
# If it is wrong, ask the typing again until it has a correct value.
gender = str(input("Enter the gender [F/M]: ")).replace(' ', '').upper()
while gender != "M" and gender != "F":
    gender = input("Invalid option. Try again. Enter the gender: ").replace(' ', ''). upper()
if gender == 'F':
    print("Female gender successfully recorded.")
else:
    print("Male gender successfully recorded.")
