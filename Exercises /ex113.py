#Python Exercise 113 In-depth functions in Python
# Rewrite the readInt() function that we created in challenge 104, now including the possibility
# of typing an invalid number. Take advantage and also create a readFloat() function with the same functionality.
from ex_modules.colours import use_colours
def readInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (TypeError, ValueError):
            print(f"{use_colours('red')}ERROR!Enter a valid integer number.{use_colours('clean')}")
        except KeyboardInterrupt:
            print(f"{use_colours('red')}\nThe user preferred not to enter any number.{use_colours('clean')}")
            return 0.0
        else:
            return num


def readFloat(txt):
    while True:
        try:
            text = input(txt).replace(',', '.')
            num = float(text)
        except (ValueError, TypeError):
            print(f"{use_colours('red')}ERROR!Enter a valid decimal number.{use_colours('clean')}")
        except KeyboardInterrupt:
            print(f"{use_colours('red')}\nThe user preferred not to enter any number.{use_colours('clean')}")
            return 0.0
        else:
            return num


int_value = readInt("Enter an integer number: ")
float_value = readFloat("Enter a decimal number: ")
print(f"You typed the integer number {int_value} and the decimal number {float_value}.")
