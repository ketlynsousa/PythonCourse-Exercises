# Python Exercise 111 - Transforming modules into packages
# Create a package that has two internal modules called coins and data.
# Transfer all the functions used in challenges 107, 108 and 109 to the first package and
# keep everything working.

#Packaging created and modules transfer done, everything working as expected

from ex_modules.coins import summary

valor = float(input("Digite um valor: R$"))
summary(valor, 15, 10)
