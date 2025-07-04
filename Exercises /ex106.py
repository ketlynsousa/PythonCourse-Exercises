# Python Exercise 106 - Interactive Python Help System
# Make a mini-system that uses Python's Interactive Help.
# The user will type the command and the manual will appear.
# When the user types the word 'END', the program will end. Important: use colours.
from time import sleep
def use_colour(colour):
    colours = {
        'clean': '\033[m',
        'red': '\033[1;30;41m',
        'green': '\033[1;30;42m',
        'blue': '\033[1;30;44m',
        'white': '\033[7;40m'
    }
    return colours[colour]

def write(txt):
    size = len(txt) + 4
    print(use_colour('green'))
    print("=" * size)
    print(f"  {txt}")
    print("=" * size)
    print(use_colour('clean'))
    sleep(1.5)
    print()

def assistance(txt):
    print(use_colour('blue'))
    print(f"Accessing the command manual \'{txt}\'...")
    print(use_colour('clean'))
    print(use_colour('white'))
    help(txt)
    print(use_colour('clean'))
    sleep(1.5)


# Main program
while True:
    write("PYTHON HELPING ASSISTANCE SYSTEM")
    command = str(input("Function or Library > "))
    if command.upper() == 'END':
        write("CLOSING THE SYSTEM...")
        break
    else:
        assistance(command)
