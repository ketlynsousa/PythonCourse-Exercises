# Python Exercise 084 - Composite list and data analysis
# Write a program that reads the name and weight in Kg of several people, saving everything in a list. At the end, show:
# A) How many people were registered.
# B) A list with the heaviest people.
# C) A list with the lightest people.
people_data = []
people_registers = []
heaviest = lightest = 0

while True:
    people_data.append(str(input("Enter your name: ")))
    people_data.append(float(input("Enter your weight: ")))
    if len(people_registers) == 0:
        heaviest = lightest = people_data[1]
    else:
        if people_data[1] < lightest:
            lightest = people_data[1]
        if people_data[1] > heaviest:
            heaviest = people_data[1]
    people_registers.append(people_data[:])
    people_data.clear()
    answer = str(input("Do you wish to continue? [Y/N] ")).strip().upper()
    while answer not in ('Y', 'N'):
        print("Invalid option.")
        answer = str(input("Do you wish to continue? [Y/N] ")).strip().upper()
    if answer == 'N':
        break

print('=*' * 30)
print(f"A total of {len(people_registers)} people were registered.")
print(f"The lightest weight was {lightest}Kg. For the person ", end='')
for person in people_registers:
    if person[1] == lightest:
        print(f"[{person[0].title()}] ", end='')
print(f"\nThe heaviest weight was {heaviest}Kg. For the person ", end='')
for person in people_registers:
    if person[1] == heaviest:
        print(f"[{person[0].title()}] ", end='')
