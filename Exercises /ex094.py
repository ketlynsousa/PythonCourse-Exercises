# Python Exercise 094 - Uniting dictionaries and lists
# Create a program that reads the name, gender and age of various people,
# Guarding the data of each person on a dictionary and all dictionaries on a list. In the end, show:
# A) How many people were registered
# B) the average age
# C) A list of women
# D) A list of people above average
register_list = []
add = age_average = 0

while True:
    register = dict()
    register['Name'] = str(input("Enter tha name: ")).strip().title()
    while True:
        register['Gender'] = str(
            input("Enter the gender: [F/M] ")).strip().upper()
        if register['Gender'] in ('F', 'M'):
            break
        print("Invalid option. ", end='')
    register['Age'] = int(input("Enter the age: "))
    register_list.append(register.copy())

    add += register['Age']
    age_average = add / len(register_list)

    while True:
        answer = str(input("Do you wish to continue: [Y/N] ")).strip().upper()
        if answer in ('Y', 'N'):
            break
        print("Invalid option.  ", end='')

    if answer == 'N':
        break

print("=*" * 30)
print("REGISTER ANALYSIS".center(60))
print("=*" * 30)
print(f"• They were registered {len(register_list)} people.")
print(f"• The average age registered is {age_average:.2f} years old.")
print(f"• The women registered are ", end='')
for person in register_list:
    if person['Gender'] == 'F':
        print(f"{person['Name']} ", end='')
print()
print(f"List of people above average age: ")
for person in register_list:
    if person['Age'] >= age_average:
        for key, value in person.items():
            print(f"{key}: {value} ", end='')
            print()
