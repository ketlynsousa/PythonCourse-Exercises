# Python Exercise 080 - Ordered list without repetitions
# Create a program where the user can enter five numeric values and register them in a list,
# already in the correct insertion position (without using sort()). At the end, display the ordered list on the screen.
import bisect
values = []
for count in range(5):
    num = int(input(f"Enter the {count + 1}º value: "))
    bisect.insort(values, num)
    print(f"The value {num} added to the position {values.index(num)}.")

print(f"Ordered values' list: {values}.")
