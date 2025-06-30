# Python Exercise 079 - Unique Values in a List
# Create a program where the user can type several numeric values and register them in a list.
# If the number already exists in there, it will not be added.
# At the end, all unique values entered will be displayed, in ascending order.
numbers_list = []

while True:
    num = int(input("Enter a number: "))
    if num not in numbers_list:
        numbers_list.append(num)
        print("Number successfully added to the list.")
    else:
        print("Number is already in the list. It will not be added.")

    resp = str(input("Do you wish to continue? [Y/N] ")).strip().upper()
    while resp not in ('Y', 'N'):
        print("Invalid Option. ", end='')
        resp = str(input("Do you wish to continue? [Y/N] ")).strip().upper()

    if resp == 'N':
        break
print("=*" * 30)
print(f"The numbers typed was {sorted(numbers_list)}.")
