# Python Exercise 065 - Largest and Smallest Values
# Create a program that reads several integers from the keyboard.
# At the end of the execution, show the average of all the values and which were the largest and smallest values.
# The program should ask the user whether he wants to continue typing values or not.
add =  cont = 0
num_list = []
while True:
    num = int(input("Enter an integer number: "))
    resp = str(input("Do you wish to continue? [Y/N] ")).strip().upper()
    if resp == 'N':
        break
    else:
        add += num
        num_list.append(num)
        average = add / len(num_list)
        largest_num = max(num_list)
        smallest_num = min(num_list)
        print(f"The average of the values {num_list} is {average:.2f}")
        print(f"The largest number of the values {num_list} is {largest_num}.")
        print(f"The smallest number of the values {num_list} is {smallest_num}.")
