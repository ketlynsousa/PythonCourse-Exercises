# Python Exercise 044 - Payment Manager
# Develop a program that calculates the amount to be paid for a product, considering its normal price and payment conditions:
# - cash/check: 10% discount
# - cash on card: 5% discount
# - up to 2x on card: normal price
# - 3x or more on card: 20% interest

product_price = float(input("Enter the product price: $"))
print(f"PAYMENT METHODS:")
payment_option = int(input(f"For payment by cash/check, press 1:"
                            f"\nFor one time payment by card, press 2:"
                            f"\nFor payment by card up to 2x, press 3:"
                            f"\nFor payment by card in 3x or more, press 4: \n"))

cash_check_payment = product_price - (product_price * 0.10)
payment_card_1 = product_price - (product_price * 0.05)
payment_card_2x = product_price
payment_card_3x = product_price + (product_price * 0.20)

if payment_option == 1:
    print(f"For check or cash payment, the product's price receives 10% discount. The total amount to be paid is ${cash_check_payment:.2f}.")
elif payment_option == 2:
    print(f"For one time card payment, the product's price receives 5% discount. The total amount to be paid is ${payment_card_1:.2f}.")
elif payment_option == 3:
    print(f"For up to 2x card installments, the product's price does not receive a discount. Total to be paid is ${payment_card_2x:.2f}.")
elif payment_option == 4:
    print(f"For 3x or more card installment, the product's price receives 20% of interest. Total to be paid is ${payment_card_3x:.2f}.")
else:
    print(f"Invalid option. Please try again.")


