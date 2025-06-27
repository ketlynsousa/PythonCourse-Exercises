# Python Exercise 013 - Salary Adjustment
# Create an algorithm that reads an employee's salary and shows their new salary, with a 15% increase.

current_salary = float(input("Enter the current salary: $"))
salary_increase = current_salary + (15/100 * current_salary)
print(f"Current salary ${current_salary:.2f} with 15% increase will be ${salary_increase:.2f}.")
