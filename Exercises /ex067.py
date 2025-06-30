# Python Exercise 067 - Times Tables v3.0
# Write a program that displays the times tables of several numbers, one at a time, for each value entered by the user.
# The program will stop when the requested number is negative.
colors = {
    'red': '\033[1;31m',
    'blue': '\033[1;34m',
    'green': '\033[1;32m',
    'clean': '\033[m'
}
while True:
    print(f"{colors['red']}Negative numbers close the system immediately.{colors['clean']}")
    num = int(input("Enter the number for which you wish to view the times table: "))
    if num < 0:
        print(f"{colors['green']}Multiplication table system closed.{colors['clean']}")
        break
    else:
        cont = 0
        while cont < 10:
            cont += 1
            result = num * cont
            print(f"{colors['blue']}{num} x {cont:2} = {result}{colors['clean']}")
