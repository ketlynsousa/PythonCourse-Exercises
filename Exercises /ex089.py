# Python Exercise 089 - Report Card with Composite Lists
# Create a program that reads the name and two grades of several students and stores everything in a composite list.
# At the end, show a report card containing the average of each one and allow the user to show
# the grades of each student individually.
full_list = []
while True:
    name = str(input("Enter the name: "))
    grade1 = float(input("Enter the first grade: "))
    grade2 = float(input("Enter the second grade: "))
    average = (grade1 + grade2) / 2
    full_list.append([name, [grade1, grade2], average])
    answer = str(input("Do you wish to continue? [Y/N] ")).strip().upper()
    while answer not in ('Y', 'N'):
        print("Invalid Option.")
        answer = str(input("Do you wish to continue? [Y/N] ")).strip().upper()
    if answer == 'N':
        break

print("=*" * 25)
print(f"{'SCHOOL REPORT CARD':^50}")
print("=*" * 25)
print(f"{'ID'} {'STUDENT':>20} {'AVERAGE':>22}")
for i, student in enumerate(full_list):
    print(f"{i} {student[0].upper():>22} {student[2]:>21.2f}")
print("=*" * 25)

while True:
    ID = int(input(
        "Enter the ID of those who you wish to know detailed notes or (999 to close): "))
    if ID == 999:
        print(f"{'SYSTEM FINISHED.':^80}")
        break
    if ID <= len(full_list):
        print("=*" * 50)
        print(
            f"Grades for the student {full_list[ID][0]} are {full_list[ID][1]}")
        print("=*" * 50)
