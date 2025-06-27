# Python Exercise 012 - Calculating Discounts
# Create an algorithm that reads the price of a product and shows its new price, with a 5% discount.

price = float(input("Product price: $"))
discount = price - (5/100 * price)
print(f"The product price with 5% of discount is {discount:.2f}.")