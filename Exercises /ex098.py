# Python Exercise 098 - Count Function
# Make a program that has a function called count (), which receives three parameters: start, end and step.
# Your program has to perform three counts through the function created:
# a) From 1 to 10, from 1 to 1
# b) From 10 to 0, from 2 to 2
# c) A personalized count

from time import sleep


def count(start, end, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    print(f"Counting from {start} to {end} with {step} as common difference.")
    sleep(2)
    if start < end:
        count = start
        while count <= end:
            print(f"{count} ", end='', flush=True)
            sleep(0.5)
            count += step
        print("--> THE END!")
    else:
        count = start
        while count >= end:
            print(f"{count} ", end='', flush=True)
            sleep(0.5)
            count -= step
        print("--> THE END!")


# Main program
count(1, 10, 1)
print()
count(10, 0, 2)
print()
print("Customize your count.")
start = int(input("Enter the start: "))
end = int(input("Enter the end: "))
step = int(input("Enter the step: "))
print()
count(start, end, step)
