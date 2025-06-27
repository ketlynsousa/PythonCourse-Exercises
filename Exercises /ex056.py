# Python Exercise 056 - Complete Analyzer
# Develop a program that reads the name, age, weight and sex of 4 people.
# Display: the average age of the group, what is the name of the oldest man and how many women are under 20 years old.
age_list = []
women_under_20 = 0
max_man_age = man_name = 0

for person in range(1, 5):
    print(f"----- person {person} -----")
    name = str(input(f"Enter the name: ")).strip().upper()
    age = int(input("Enter the age: "))
    gender = str(input("Enter the gender [F/M]: ")).strip().upper()
    age_list.append(age)
    if age < 20 and gender == 'F':
        women_under_20 += 1
    if person == 1 and gender == 'M':
        max_man_age = age
        man_name = name
    if gender == 'M' and age > max_man_age:
        max_man_age =  age
        man_name = name
average_age = sum(age_list) / len(age_list)

print("----- ANALYZING DATA -----")
print(f"\nThe average age of the group is {average_age:.2f}.")
print(f"\nThe name of the oldest man in the group is {name} and has {age} years.")
print(f"\nThere is {women_under_20} women under 20s in the group.")
