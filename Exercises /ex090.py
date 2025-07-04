# Python Exercise 090 - Dictionary
# Make a program that reads a student's name and average, also keeping the situation in a dictionary.
# In the end, show the content of the structure on the screen.

student = {}
name = str(input("Student's name: "))
average = float(input(f"{name.title()}'s average grade: "))
student['Name'] = name
student['Average'] = average
if student['Average'] > 7:
    student['Situation'] = 'Approved'
elif student['Average'] < 5:
    student['Situation'] = 'Reproved'
else:
    student['Situation'] = 'Recovery'
print("=*" * 30)
for key, value in student.items():
    print(f"    - {key} is {value}.")
