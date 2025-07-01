# Python Exercise 082 - Unique Values in a List
# Create a program that will read several numbers and put them in a list.
# After that, create two extra lists that will contain only the even values and the odd values entered, respectively.
# At the end, show the contents of the three lists generated.
numbers_list = list()

while True:
    numbers_list.append(int(input("Enter a value: ")))
    answer = str(input("Do you wish to continue? [Y/N] ")).upper().strip()
    while answer not in ('Y', 'N'):
        print("Invalid Option. ",end='')
        answer = str(input("Do you wish to continue? [Y/N] ")).upper().strip()
    if answer == 'N':
        break

even_list = [num for num in numbers_list if num % 2 == 0]
odd_list = [num for num in numbers_list if num % 2 == 1]

print("=*" * 30)
print(f"Full list: {numbers_list}.")
print(f"List only with even numbers: {even_list}.")
print(f"List only with odd numbers: {odd_list}.")
