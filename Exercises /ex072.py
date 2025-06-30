# Python Exercise 072 - Number in Words
# Create a program that has a tuple completely filled with a count in words, from zero to twenty.
# Your program should read a number from the keyboard (between 0 and 20) and display it in words.

numbers_written_form = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
           'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',)
position = -1
while position < 0 or position > 20:
    position = int(input("Enter a number from 0 to 20: "))
print(f"You typed the number {numbers_written_form[position]}.")
