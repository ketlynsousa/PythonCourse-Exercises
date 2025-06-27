# Python Exercise 010 - Currency Converter
# Create a program that reads how much money a person has in their wallet in Brazilian Real and shows how many Dollars they can buy.
# Consider the dollar at USD1.00 = R$5.27

br_real = float(input("How much would you like to convert? R$"))
dollar = br_real / 5.27
print("Considering the dollar at R$5.27...")
print(f"With R${br_real} you can purchase {dollar:.2f} dollars. ")
