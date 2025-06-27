# Python Exercise 019 - Drawing an item from the list
# A teacher wants to draw one of his four students to erase the board.
# Write a program that helps him by reading the students' names and writing the name of the chosen one on the screen.
import random

name1 = str(input("First student's name: "))
name2 = str(input("Second student's name: "))
name3 = str(input("Third student's name: "))
name4 = str(input("Fourth student's name: "))
name_list = [name1, name2, name3, name4]
print(f"The names added were {name_list}.\nThe chosen one to erase the board was {random.choice(name_list)}.")