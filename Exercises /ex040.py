# Python Exercise 040 - That classic Average
# Create a program that reads two grades from a student and calculates their average,
# showing a message at the end, according to the average achieved:
# - Average below 5.0: FAILED
# - Average between 5.0 and 6.9: RECOVERY CLASS
# - Average 7.0 or higher: PASSED
colors = {'red': '\033[1;31m',
          'green': '\033[1;32m',
          'yellow': '\033[1;33m',
          'title': '\033[1;4m',
          'clean': '\033[m'}

print(f"{colors['title']}Let's find out the grade for the last two exams!{colors['clean']}")

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
average: float = (grade1 + grade2) / 2

if average < 5.0:
    print(f"Your grade average is {average:.1f}. {colors['red']}YOU FAILED!!!")
elif  6.9 > average >= 5.0:
    print(f"Your grade average is {average:.1f}. {colors['yellow']}YOU'RE IN RECOVERY CLASS!!!")
else:
    print(f"Your grade average is {average:.1f}. {colors['green']}CONGRATULATIONS!!! YOU'RE APPROVED.")
