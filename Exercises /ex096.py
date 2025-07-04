# Python Exercise 096 - Function that calculates area
# Make a program that has a function called area (), which receives the dimensions of a rectangular land
# (width and length) and show the area of ​​the land.
def area(a, b):
    m2 = b * a
    print(f"The area of a land {a}x{b} is of {m2}m².")


def heading(txt):
    print("=*" * 20)
    print(txt.center(40))
    print("=*" * 20)


heading("LAND CONTROL")

width = float(input("Enter the windth (m²): "))
length = float(input("Enter the length(m²): "))
area(width, length)
