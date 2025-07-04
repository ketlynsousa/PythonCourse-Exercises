# Python Exercise 102 - Function for Factorial
# Create a program that has a factorial() function that receives two parameters:
# the first one indicating the number to calculate and another one called show, which will be a logical value (optional)
# indicating whether or not the factorial calculation process will be shown on the screen.

def factorial(num=1, show=False):
    """
    The function receives two values, one mandatory that returns the factorial of a number and another (optional)
    that shows the calculation process.
    :param num: It should receive an integer number and calculate the factorial
    :param show: Displays the calculation process and result
    :return: Returns the factorial of num
    """
    fact = 1
    for count in range(num, 0, -1):
        if show:
            fact *= count
            print(count, end='')
            if count > 1:
                print(" x ", end='')
            else:
                print(" = ", end='')
        else:
            fact *= count
    return fact


print("=*" * 25)
print("FACTORIAL CALCULATION".center(50))
print("=*" * 25)
value = int(input("Enter the value you want to know the factorial of: "))
print(f'The factorial of {value} is {factorial(value, show=False)}.')
while True:
    answer = str(input(
        f"Do you wish to display the factorial calculation process? [Y/N] ")).strip().upper()
    if answer in 'Y':
        print(f"Factorial calcultation of {value} = ", end='')
        print(f"{factorial(value, show=True)}.")
        break
    else:
        if answer == 'N':
            print("SYSTEM CLOSED.")
            break
