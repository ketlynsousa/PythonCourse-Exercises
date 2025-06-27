# Python Exercise 036 - Approving a Loan
# Write a program to approve a bank loan to buy a house. Ask for the value of the house,
# the buyer's salary and in how many years he will pay it off.
# The monthly payment cannot exceed 30% of the salary or else the loan will be denied.
from math import ceil

house_price = float(input("Enter the price of the house: "))
salary = float(input("Enter your monthly income: "))
payment_years = int(input("Indicate how many years you want to pay off the loan: "))

payment_months = payment_years * 12
instalments = house_price / payment_months

if instalments > 0.30 * salary:
    min_months = house_price / (0.30 * salary)
    min_years = ceil(min_months / 12)
    print(f"The instalments would be {instalments:.2f}, which is higher than 30% of your salary."
          f"\n\033[1;31mLoan denied:\033[m you can't take this loan for just {payment_years} years."
          f"\nTo make it work, you'd need at least {min_years} years of loan at your current salary.")
else:
    print(f"The instalments would be {instalments:.2f} for a loan of {payment_years} years. "
          f"\n\033[1;32mLoan accepted.\033[m You can proceed to loan agreement.")

