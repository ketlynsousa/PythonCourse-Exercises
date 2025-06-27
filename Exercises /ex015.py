# Python Exercise 015 - Car Rental
# Write a program that asks for the number of kilometers traveled by a rented car and the number of days for which it was rented.
# Calculate the price to pay, knowing that the car costs $60 per day and R$0.15 per kilometer driven.

kilometers = float(input("Enter kilometers traveled: "))
days_rented = int(input("Enter days traveled: "))
total_price = (60 * days_rented) + (kilometers * 0.15)
print(f"Total price to pay is ${total_price}.")
