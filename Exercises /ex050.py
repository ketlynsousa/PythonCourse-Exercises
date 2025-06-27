# Python Exercise 050 - Sum of pairs
# Develop a program that reads six integers and displays the sum of only those that are even.
# If the value entered is odd, disregard it.
plus = cont = 0
for num in range(1, 7):
    n = int (input(f"Enter the number: "))
    if n % 2 == 0:
        plus += n
        cont += 1
print(f"You entered {cont} even numbers. The sum of the even numbers is {plus}.")
