# Python Exercise 064 - Arithmetic Progression V2.0
# Write a program that reads an integer number and shows on the screen
# The first N numbers of Fibonacci sequence.
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
print("-=" * 10)
print("FIBONACCI SEQUENCE")
print("-=" * 10)
num = int(input("Enter how many terms you want to display: "))

term1 = 0
term2 = 1
print(f"{term1} → {term2} → ", end='')
cont = 3
while cont < num:
    term3 = term1 + term2
    print(f"{term3} → ", end='')
    term1 = term2
    term2 = term3
    cont += 1
print("THE END!")
