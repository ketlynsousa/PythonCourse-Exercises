def use_colours(colour):
    colours = {
        'clean': '\033[m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'gray': '033[37m',
        'bold': '\033[1m',
        'underline': '\033[4m'
    }
    return colours[colour]

def readInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print(f"{use_colours('red')}ERROR!Enter a valid integer number.{use_colours('clean')}")
        except KeyboardInterrupt:
            print(f"{use_colours('red')}\nThe user preferred not to enter any number.{use_colours('clean')}")
            break
        else:
            return num

def line():
    print('=*'* 21)

def heading(txt):
    line()
    print(txt.center(42))
    line()


def menu(lst):
    count = 1
    for item in lst:
        print(f"{use_colours('magenta')}{count}{use_colours('clean')} - {use_colours('blue')}{item}{use_colours('clean')}")
        count += 1
    line()
    answer = readInt(f'{use_colours('magenta')}\nEnter one option: {use_colours('clean')}')
    return answer
