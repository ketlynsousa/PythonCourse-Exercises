# Python Exercise 058 - V2.0 Divination Game
# Improve the challenge game 028 where the computer will "think" in a number between 0 and 10.
# Only now the player will try to guess until he got it right, # showing at the end
# How many guesses took to win.

from random import randint
from time import sleep
import emoji

right_hits = False
attempts = 0

#game introduction
print("\033[1;35m = \033[m" * 20)
print("Let's play GUESS the number GAME.".center(60))
print("\033[1;35m = \033[m" * 20)

#computer choice
computer_choice = randint(0, 10)
print("I thought of a number between 0 to 10. Try to guess!\n")

#loop of attempts with conditions to win or lose the game.
while not right_hits:
    player_choice = int(input("Type: "))
    attempts += 1
    print(emoji.emojize("\033[33mDo you think you nailed it???\033[m 😰😰😰\n", language='alias'))
    sleep(2.5)

    if player_choice == computer_choice:
        right_hits = True
        print(emoji.emojize(f"\033[1;32mCongratulations! You got it right!!!\nWith {attempts} attempts.\033[m", language='alias'))
        break
    else:
        if player_choice < computer_choice:
            print(emoji.emojize(f"\033[1;31mYou got WRONG!!!\nType a larger value... Try again.\033[m😢""", language='alias'))
        elif player_choice > computer_choice:
            print(
                emoji.emojize(f"\033[1;31mYou got WRONG!!!\nType a lower value... Try again.\033[m😢""", language='alias'))
