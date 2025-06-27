# Python Exercise 061 - Arithmetic Progression v2.0
# Create a program that reads several integers from the keyboard.
# The program will only stop when the user types the value 999, which is a stopping condition.
# At the end, show how many numbers were typed and what was the sum between them (disregarding the flag).
add = 0
cont = 0
while True:
    num = int(input("Enter a number or [999] to exit: "))
    cont += 1
    if num == 999:
        break
    else:
        add += num
print(f"You entered {cont - 1} numbers and the sum of the values informed is {add}.")
