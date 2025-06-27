# Python Exercise 047 - Counting pairs
# Create a program that displays on the screen all the even numbers that are in the range between 1 and 50.

print("\nDISPLAYING EVEN NUMBERS IN THE RANGE FROM 0 TO 50.\n")
for num in range(2, 51):
    if num % 2 == 0:
        print(num, end=" ")
print("\nTHE END!")
