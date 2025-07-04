def currency(num: float):
    return f'${num:.2f}'.replace('.', ',')


def double(num=0, formatted=False):
    result = num * 2
    if formatted:
        return currency(result)
    else:
        return result


def half(num=0, formatted=False):
    result = num / 2
    if formatted:
        return currency(result)
    else:
        return result


def increase(num=0, perc=0, formatted=False):
    result = num + (perc / 100) * num
    if formatted:
        return currency(result)
    else:
        return result

def decrease(num=0, perc=0, formatted=False):
    result = num - (perc / 100) * num
    if formatted:
        return currency(result)
    else:
        return result

def summary(num=0, more=0, less=0):
    print('=*' * 20)
    print('PRICE SUMMARY'.center(40))
    print('=*' * 20)
    print(f'Value analysed:   \t\t\t\t{currency(num)}')
    print(f'Double of the value:   \t\t\t{double(num, True)}')
    print(f'Half of the value:   \t\t\t{half(num, True)}')
    print(f'Increase of {more}%:   \t\t\t\t{increase(num, more, True)}')
    print(f'Decrease of {less}%:   \t\t\t\t{decrease(num, less, True)}')
    print("=*" * 20)
