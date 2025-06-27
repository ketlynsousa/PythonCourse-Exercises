# Python Exercise 023 - Separating digits from a number
# Write a program that reads a number from 0 to 9999 and displays each of the separated digits on the screen.
#EX: Enter the number: 1834 return Unit: 4 - Tens: 3 - Hundreds: 8 - Thousands: 1

number = int(input("Enter any number from 0 to 9999: "))
print(f"Analysing the number {number}...")
print(f"Unit: {number // 1 % 10}")
print(f"Tens: {number // 10 % 10}")
print(f"Hundreds: {number // 100 % 10}")
print(f"Thousands: {number // 1000 % 10}")
