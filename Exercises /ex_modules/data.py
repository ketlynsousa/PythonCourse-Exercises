def readMoney(txt):
    while True:
        price = input(txt).replace(',', '.').strip()
        if price.isalpha() and price.isalnum():
            print(f"\033[1;31mERROR! The price {price} is an invalid value.\033[m")
        elif price == '':
            print(f"\033[1;31mERROR! The price {price} is an invalid value!\033[m")
        else:
            return float(price)
