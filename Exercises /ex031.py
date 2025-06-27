# Python Exercise 031 - Travel Cost
# Develop a program that asks for the distance for a trip to in km.
# Calculate the price of the ticket, charging R$0.50 per km for trips up to 200 km and R$0.45 for longer trips.

distance = float(input("How far is your trip? "))
print(f"You are about to start a journey of {distance:.1f}Km.")
if distance <= 200:
    print(f"The price of the ticket is ${0.50 * distance:.2f}.")
else:
    print(f"The price of the ticket is {0.45 * distance:.2f}.")
