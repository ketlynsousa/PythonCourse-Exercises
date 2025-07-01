# Python Exercise 081 - Extracting data from a list
# Create a program that will read several numbers and put them in a list. After that, show:
# A) How many numbers were entered.
# B) A list of values, ordered in descending order.
# C) Whether the value 5 was entered and is or is not in the list.

numbers_list = list()

while True:
    numbers_list.append(int(input("Enter a value: ")))
    answer = str(input("Do you wish to continue? [Y/N] ")).upper().strip()
    while answer not in ('Y', 'N'):
        print("Invalid option.")
        answer = str(input("Do you wish to continue? [Y/N] ")).upper().strip()
    if answer == 'N':
        break
print("=*" * 30)
print(f"You typed {len(numbers_list)} numbers.")
numbers_list.sort(reverse=True)
print(f"List of numbers in decreasing format: {numbers_list}.")

if 5 in numbers_list:
    print("You entered the number 5 and It's in the list.")
else:
    print("You haven't entered the number 5 and It's not in the list.")
