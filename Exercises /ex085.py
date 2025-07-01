# Python Exercise 085 - Lists with even and odd numbers
# Create a program where the user can enter seven numeric values and register them in a single list
# that keeps even and odd values separate.
# At the end, show the even and odd values in ascending order.
numbers_list = [[], []]

for count in range(0, 7):
    num = int(input(f"Enter the {count + 1}º number: "))
    if num % 2 == 0:
        numbers_list[0].append(num)
    else:
        numbers_list[1].append(num)

print(f"The even numbers in ascending order are {sorted(numbers_list[0])}.")
print(f"The odd numbers ascending order are {sorted(numbers_list[1])}.")
