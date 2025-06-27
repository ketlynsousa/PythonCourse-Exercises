# Python Exercise 049 - Times Tables v.2.0
# Redo CHALLENGE 009, showing the times table of a number that the user chooses, but now using a for loop.

num = int(input("Enter a number to display its times table: "))
print("\033[35m=*\033[m" * 15)
for cont in range(1, 11):
    result = num * cont
    print(f"\033[34m{num} x {cont:2} = {result}\033[m")
print("\033[35m=*\033[m" * 15)
