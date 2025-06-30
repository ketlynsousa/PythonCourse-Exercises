# Python Exercise 075 - Data Analysis in a Tuple
# Develop a program that reads four values from the keyboard and stores them in a tuple. At the end, show:
# A) How many times the value 9 appeared.
# B) In which position was the first value 3 typed.
# C) Which were the even numbers.
values = (
    int(input("Enter the 1st value: ")),
    int(input("Enter the 2nd value: ")),
    int(input("Enter the 3rd value: ")),
    int(input("Enter the 4th value: ")),
)
print("\t")
print(f"The number 9 appeared {values.count(9)} time(s).")
if 3 in values:
    print(f"The number 3 was first time typed in positon {values.index(3) + 1}.")
else:
    print("The number 3 was not typed.")

even__numbers = tuple(num for num in values if num % 2 == 0)
print(f"The even numbers typed was: {even__numbers if even__numbers else 'No even numbers found'}.")
