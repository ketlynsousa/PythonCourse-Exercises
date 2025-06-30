# Python Exercise 074 - Largest and smallest values in a tuple
# Create a program that will generate five random numbers and put them in a tuple.
# After that, show the list of generated numbers and also indicate the smallest and largest values that are in the tuple.
from random import randint
random_numbers = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
)
print(f"The numbers randomly generated was {random_numbers}.")
print(f"The smallest number generated was {min(random_numbers)}.")
print(f"The largest number generated was {max(random_numbers)}.")
