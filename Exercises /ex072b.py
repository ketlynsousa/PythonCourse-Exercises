# Second version for exercise 072
# This version I used num2words library.

from num2words import num2words
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

answer = int(input("Enter a number from 0 to 20: "))
while True:
    if answer not in numbers:
        print("\033[31mInvalid option. Try again\033[m")
        answer = int(input("Enter a number from 0 to 20: "))
    else:
        if answer in numbers:
            written_form = num2words(answer, lang='en')
            print(f"\nYou typed the number {written_form}.")
            break
