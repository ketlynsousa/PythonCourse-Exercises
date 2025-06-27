# Python Exercise 028 - Guessing Game v.1.0
# Write a program that makes the computer "think" of an integer between 0 and 10
# and asks the user to try to figure out which number the computer chose.
# The program should write on the screen whether the user won or lost.

from random import randint
from time import sleep
import emoji

print("\033[1;35m = \033[m" * 20)
print(f"{'LETS PLAY GUESS THE NUMBER GAME':^60}")
print("\033[1;35m = \033[m" * 20)

computer_choice = randint(0, 5)
player_choice = int(input("Try to guess the number I picked from 0 to 5: "))

print(emoji.emojize("\033[33mWHO WILL BE THE WINNER?\033[m 😰😰😰\n", language='alias'))
sleep(3)

if player_choice == computer_choice:
    print(emoji.emojize(f"You chose the number {player_choice}. The computer chose {computer_choice}."
                        f"\n\033[1;32mCongratulations! You WON!!!\033[m🤓", language='alias'))
else:
    print(emoji.emojize(f"You chose the number {player_choice}. The computer chose {computer_choice}."
                        f"\n\033[1;31mYou got WRONG!!!\033[m😢", language='alias'))

