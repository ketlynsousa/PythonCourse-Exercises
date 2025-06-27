# Python Exercise 052 - Prime Numbers
# Write a program that reads an integer and tells whether it is a prime number or not.

prime = int(input("Enter an integer number: "))
cont = 0

for num in range(1, prime + 1):
    if prime % num == 0:
        cont += 1
        print("\033[1;32m", end='')
    else:
        print("\033[1;33m", end='')
    print(num, end=' ')

if cont == 2:
    print(f"\033[m\nThe number {prime} is divisible by {cont} numbers.\nTherefore it is a prime number.")
else:
    print(f"\033[m\nThe number {prime} is divisible by {cont} numbers.\nTherefore it is NOT a prime number.")
