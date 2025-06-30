# Python Exercise 070 - Statistics on products
# # Create a program that reads the name and price of several products.
# # The program should ask the user whether to continue or not. At the end, display:
# # A) what is the total spent on the purchase.
# # B) how many products cost more than $1000.
# # C) what is the name of the cheapest product.
total_shopping = more_1000 = count = cheapest_price = 0
cheapest_product = ''

print("=" * 60)
print(f"{'SHOPPING REGISTER':^60}")
print("=" * 60)

#REGISTERING PRICES
while True:
    product_name = str(input("Product's name: ")).strip().upper()
    product_price = float(input("Price: $"))
    print("\033[32mREGISTERED SUCCESSFULLY.\033[m")
    count += 1

    #option to continue registering
    register = str(input("Do you wish to continue: [Y/N] ")).strip().upper()[0]
    while register not in ("Y", "N"):
        print("Invalid option. Try again.")
        register = str(input("Do you wish to continue: [Y/N] ")).strip().upper()[0]

    #counters
    total_shopping += product_price

    if product_price > 1000:
        more_1000 += 1

    if count == 1:
        cheapest_price = product_price
        cheapest_product = product_name
    else:
        if product_price < cheapest_price:
            cheapest_price = product_price
            cheapest_product = product_name

    #finishing loop
    if register == 'N':
        print("\033[34mSYSTEM CLOSED.\033[m")
        break

#registering analysis
print("=" * 60)
print(f"{'SHOPPING ANALYSES':^60}")
print("=" * 60)
print(f"Total amount spent was \033[33m{total_shopping:.2f}.\033[m")
print(f"\033[33m{more_1000}\033[m products cost more than $1000 dollars.")
print(f"The cheapest product name is \033[33m{cheapest_product}\033[m and it costs \033[33m${cheapest_price:.2f}\033[m.")
