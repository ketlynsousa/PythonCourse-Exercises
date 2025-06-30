# Python Exercise 071 - ATM Simulator
# Create a program that simulates the operation of an ATM.
# At the beginning, ask the user what amount will be withdrawn (integer)
# and the program will inform how many bills of each value will be delivered.
# NOTE: consider that the ATM has bills of $50, $20, $10 and $1.
print("=" * 25)
print(f"{'ATM':^25}")
print("=" * 25)

withdrawn_amount = int(input("How much do you want to withdraw? "))
total = withdrawn_amount
money_notes = 50
counting_notes = 0

while True:
    if total >= money_notes:
        total -= money_notes
        counting_notes += 1
    else:
        if counting_notes > 0:
            print(f"A total of {counting_notes} - {money_notes} dollar notes.")
        if money_notes == 50:
            money_notes = 20
        elif money_notes == 20:
            money_notes = 10
        elif money_notes == 10:
            money_notes = 1
        counting_notes = 0

        if total == 0:
            break
