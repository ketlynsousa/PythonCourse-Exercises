# Python Exercise 058 - V2.0 Divination Game
# Create a program that reads two values and display a menu on the screen:
# [1] add
# [2] Multiply
# [3] Bigger
# [4] New numbers
# [5] Exit the program
#  Your program must carry out the required procedure in each situation.
from time import sleep

value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
option = 0

while option != 5:
    print("  -----OPTIONS-----\n"
          "[ 1 ] ADD\n"
          "[ 2 ] MULTIPLY\n"
          "[ 3 ] BIGGER\n"
          "[ 4 ] NEW NUMBERS\n"
          "[ 5 ] EXIT THE PROGRAM\n", end='')
    print("=*" * 15)
    option = int(input("Enter the option number: "))
    if option == 1:
        add = value1 + value2
        print(f"The sum of {value1} + {value2} is equal to {add}.")
    elif option == 2:
        product = value1 * value2
        print(f"The product of {value1} x {value2} is equal to {product}.")
    elif option == 3:
        if value1 > value2:
            biggest_value = value1
        else:
            biggest_value = value2
        print(f"The biggest value between {value1} and {value2} is {biggest_value}.")
    elif option == 4:
        value1 = int(input("Enter the first value: "))
        value2 = int(input("Enter the second value: "))
    elif option ==5:
        print("Finalizing the program...")
        sleep(1.5)
        print("Program finalized successfully.")
    else:
        print("Invalid option. Try again.")
    sleep(2)
