# Python Exercise 020 - Sorting an order in the list
# The same teacher from challenge 019 wants to sort the order of the presentation of students' work.
# Write a program that reads the names of the four students and shows the order drawn.
from random import shuffle
name_list = []
name1 = str(input("First student's name: "))
name2 = str(input("Second student's name: "))
name3 = str(input("Third student's name: "))
name4 = str(input("Fourth student's name: "))

name_list.append(name1)
name_list.append(name2)
name_list.append(name3)
name_list.append(name4)

print(f"The names added to the list were: {name_list}")
shuffle(name_list)
print(f"The order drawn is {name_list}.")
