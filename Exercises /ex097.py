# Python Exercise 097 - A Special Print
# Make a program that has a function called Write (),
# Let us receive any text as a parameter and show a message with adaptable size.

def write(txt):
    size = len(txt) + 6
    print("˜" * size)
    print(txt.center(size))
    print("˜" * size)
    print()


# Main proram
write("Hello, World!")
write("Python course in Youtube.")
write("I'm studying Python programming with 'Curso em Video'")
