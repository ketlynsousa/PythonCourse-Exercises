# Python Exercise 055 - Largest and smallest in the sequence
# Write a program that reads the weight of five people. At the end, show which was the largest and smallest weight read.

weight_list = []
for num in range(1, 6):
    weight = float(input(f"Enter your {num}º weight: "))
    weight_list.append(weight)
print("\n")
print(f"The biggest weight read was {max(weight_list)}Kg")
print(f"The lowest weight read was {min(weight_list)}Kg")
