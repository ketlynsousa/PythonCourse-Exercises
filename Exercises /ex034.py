# Python Exercise 034 - Multiple Raises
# Write a program that asks an employee for their salary and calculates the amount of their raise.
# For salaries greater than R$1250.00, calculate a 10% raise. For those lower or equal, the raise is 15%.

current_salary = float(input("Enter your current salary: $"))

if current_salary > 1250:
    new_salary = + current_salary + (current_salary * 0.10)
    print(f"With an increase of \033[4m10%\033[m the salary will go from \033[1;31m{current_salary:.2f}\033[m to \033[1;32m{new_salary:.2f}.")
else:
    new_salary = current_salary + (current_salary * 0.15)
    print(f"With an increase of \033[4m15%\033[m the salary will go from \033[1;31m{current_salary:.2f}\033[m to \033[1;32m{new_salary:.2f}.")
