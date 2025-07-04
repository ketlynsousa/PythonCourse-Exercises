# Python Exercise 109 - Formatting Coins
# Modify the functions that were created in challenge 107 so that they accept an additional parameter,
# informing whether the value returned by them will be formatted by the currency() function or not, developed in challenge 108.
from ex_modules import coins

price = float(input("Enter a price: $"))
print(f"The half of {coins.currency(price)} is {coins.half(price, True)}")
print(f"The double of {coins.currency(price)} is {coins.double(price, True)}")
print(f"10% more of{coins.currency(price)} is {coins.increase(price, 10, True)}")
print(f"15% less of  {coins.currency(price)} is {coins.decrease(price, 15, True)}")
