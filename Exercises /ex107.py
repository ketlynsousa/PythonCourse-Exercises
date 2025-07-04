# Python Exercise 107 - Exercising modules in Python
# Create a module called coin.py that has the built-in functions increase(), decrease(), double() and half().
# Also make a program that imports this module and uses some of these functions.
from ex_modules import coins

price = float(input("Enter a price: $"))
print(f"The half of ${price} is ${coins.half(price)}")
print(f"The double of ${price} is ${coins.double(price)}")
print(f"25% more of ${price} is ${coins.increase(price, 25)}")
print(f"25% less of ${price} is ${coins.decrease(price, 25)}")
