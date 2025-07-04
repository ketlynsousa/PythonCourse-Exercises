# Python Exercise 104 - Validating data input in Python
# Create a program that has the readInt() function, which will work in a similar way to Python's input() function,
# but validating to accept only integer numeric values.

def readInt(txt):
    while True:
        num = input(txt)
        if num.isdigit():
            return int(num)
        else:
            print("\033[31mERROR!Enter a valid integer number.\033[m")


# Main program
num = readInt("Enter a number: ")
print(f"You typed the number {num}.")
