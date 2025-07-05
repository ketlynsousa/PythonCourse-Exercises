# Python Exercise 115 - Creating a menu
# Let's create a menu in Python, using modularization, we will also see how to create and use files using Python.

from ex115_package.interface import *
from ex115_package.archives import *
from time import sleep

file_name = 'ex115_recording_file.txt'

heading('REGISTRATION SYSTEM')
while True:
    answer = menu(['REGISTER USER', 'LIST REGISTRATION', 'EXIT THE SYSTEM'])
    if answer == 1:
        # Option to register people in the txt file
        heading("NEW REGISTRATION")
        name = str(input("Enter the name: ")).strip().title()
        age = readInt("Enter the age: ")
        record(file_name, name, age)
        print(f"{use_colours('green')}{name} recorded successfully {use_colours('clean')}.")
    elif answer == 2:
        # Option to access the txt file and show the records
        readFile(file_name)
    elif answer == 3:
        # Option to log out of the system
        heading(f"SYSTEM CLOSED...")
        break
    else:
        # Option if you typed something invalid into the system
        print(f"{use_colours('red')}ERROR! Enter a valid option.{use_colours('clean')}")
    sleep(2)
