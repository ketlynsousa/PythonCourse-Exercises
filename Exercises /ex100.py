# Python Exercise 099 - Functions to draw and add
# Write a program that has a list called numbers and two functions called draw() and sumEven().
# The first function will draw 5 numbers and place them inside the list and the second function will show
# the sum between all the even values ​​drawn by the previous function.

from random import randint
from time import sleep


def draw(lst):
    print(f"The values drawn were: ", end='')
    for n in range(0, 5):
        n = randint(1, 10)
        numbers_drawn.append(n)
        print(f"{n} ", end='', flush=True)
        sleep(0.5)


def sumEven(lst):
    sleep(1)
    sum_evens = sum([n for n in lst if n % 2 == 0])
    print(f"\nThe sum of the even numbers of the list {lst} is {sum_evens}.")


# Programa principal
numbers_drawn = list()
draw(numbers_drawn)
sumEven(numbers_drawn)
