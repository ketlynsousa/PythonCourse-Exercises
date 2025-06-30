# Python Exercise 078 - Largest and Smallest Values in a List
# Write a program that reads 5 numeric values and stores them in a list.
# At the end, show which was the largest and smallest value entered and their respective positions in the list.
values = []
pos_smallest = []
pos_largest = []

for count in range(0, 5):
    values.append(int(input(f"Enter a value for the position {count}: ")))
smallest_value = min(values)
largest_value = max(values)
print("=*" * 30)
print(f"You typed the values {values}.")
print('\t')
for pos, value in enumerate(values):
    if value == smallest_value:
        pos_smallest.append(pos)
    if value == largest_value:
        pos_largest.append(pos)
print(f"The smallest value typed was {smallest_value} in the position(s) {pos_smallest}.")
print(f"The largest value typed was  {largest_value} in the position(s) {pos_largest}.")
