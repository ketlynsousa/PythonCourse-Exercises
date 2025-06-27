# Python Exercise 060 - Factorial Calculation
# Make a program that reads any number and show your factorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

print("--- FACTORIAL CALCULATION ---")
num = int(input("Enter an integer number: "))
fact = 1
cont = num
print(f"Calculating the factorial of {num}...")
for n in range(cont, 0, -1):
    print(f"{n}", end='')
    print(" x " if n > 1 else " = ", end='')
    fact *= cont
    cont -= 1
print(fact)
