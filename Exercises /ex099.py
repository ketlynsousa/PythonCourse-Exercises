# Python Exercise 099 - Function that finds the largest
# Write a program that has a function called largest(), which receives several parameters with integer values.
# Your program has to analyze all the values ​​and say which one is the largest.

from time import sleep


def largest(* num):
    print("=*" * 25)
    print("VALUES ANALYSIS...")
    if len(num) == 0:
        print("No value were informed.")
        print("=*" * 25)
        print()
        sleep(2)
    else:
        for n in num:
            print(f"{n} ", end='')
            sleep(0.5)
        print(f"\nIt was informed {len(num)} numbers.")
        print(f"The largest number informed is {max(num)}.")
        print("=*" * 25)
        print()
        sleep(2)


largest(1, 5, 4, 10, 6, 7, 2)
largest(1, 19, 20, 2, 4)
largest(1, 2)
largest(6)
largest()
