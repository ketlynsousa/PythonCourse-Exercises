# Python Exercise 066 - Multiple numbers with flag v3.0
# Create a program that reads integers from the keyboard.
# The program will only stop when the user enters the value 999, which is the stopping condition.
# At the end, show how many numbers were entered and what the sum of them was (disregarding the flag).
add = cont = 0

while True:
    num = int(input("Enter a number or (999) to exit: "))
    if num == 999:
        break
    cont += 1
    add += num
print(f"You entered {cont} values and the sum is {add}.")
