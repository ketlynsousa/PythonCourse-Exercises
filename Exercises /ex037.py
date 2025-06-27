# Python Exercise 037 - Number Base Converter
# Write a Python program that reads any integer and asks the user to choose the conversion base:
# 1 for binary, 2 for octal and 3 for hexadecimal.

number = int(input("Enter the number you want to convert to:\n"))
choice = int(str(input("Choose to convert the number from the following list:\n"
                   "Press '1' to convert to binary number:\n"
                   "Press '2' to convert to octal number:\n"
                   "Press '3' to convert to hexadecimal:\n")))

if choice == 1:
    binary = bin(number)
    print(f"The binary number for {number} is \033[1m{binary[2:]}.\033[m")
elif choice == 2:
    octal =oct(number)
    print(f"The octal number for {number} is \033[1m{octal[2:]}.\033[m")
elif choice == 3:
    hexadecimal = hex(number)
    print(f"The hexadecimal number for {number} is \033[1m{hexadecimal[2:]}. \033[m")
else:
    print("Invalid choice. Try again.")



