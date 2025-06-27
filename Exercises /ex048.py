# Python Exercise 048 - Sum of odd multiples of three
# Write a program that calculates the sum of all numbers that are multiples of three
# and that are in the range from 1 to 500.
cont = adder = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        adder += num
        cont += 1
print(f"There are {cont} numbers that are multiples of 3 and the sum of them is {adder}.")
