# Python Exercise 007 - Arithmetic Mean
# Develop a program that reads a student's two grades, calculates and displays their average.

grade1 = float(input("Type the first grade: "))
grade2 = float(input("Type the second grade: "))
average = (grade1 + grade2) / 2
print(f"The student average grade is {average:.1f}.")
