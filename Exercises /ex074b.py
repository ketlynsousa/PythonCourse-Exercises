# Second version of exercise 072
# This version instead of use the randint function 5 times, I just used sample to get 5 numbers out of a range from 0, 10.
from random import sample

numbers = range(1, 11)
random_numbers = (sample(numbers, k = 5))

print(f"The numbers randomly generated was: {random_numbers}.")
print(f"The smallest number generated was: {min(random_numbers)}.")
print(f"The largest number generated was: {max(random_numbers)}.")
