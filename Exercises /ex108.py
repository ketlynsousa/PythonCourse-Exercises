# Python Exercise 108 - Formatting Currencies
# Adapt the code from challenge #107, creating an additional function called currency() that can display the
# numbers as a formatted monetary value.
from ex_modules import coins

price = float(input("Enter a price: $"))
print(f"The half of {coins.currency(price)} is {coins.currency(coins.half(price))}")
print(f"The double of {coins.currency(price)} is {coins.currency(coins.double(price))}")
print(f"10% more of {coins.currency(price)} is {coins.currency(coins.increase(price, 10))}")
print(f"10% less of {coins.currency(price)} is {coins.currency(coins.decrease(price, 10))}")
