# Python Exercise 112 - Monetary data input
# Within the package we created in challenge 111, we have a module called data.
# Create a function called readMoney() that is capable of working like the input() function,
# but with data validation to accept only monetary values.
from ex_modules.coins import summary
from ex_modules.data import readMoney

price = readMoney("Enter the price: $")
summary(price, 15, 10)
