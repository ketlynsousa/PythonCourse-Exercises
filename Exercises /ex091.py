# Python Exercise 091 - Python Given Game
# Create a program where 4 players play a dice and have random results.
# Keep this results in a python dictionary.
# Finally, puts this dictionary in order, knowing that who won got the largest number on the dice.

from random import randint
from operator import itemgetter
from time import sleep
dice_rolls = {
    'player 1': randint(1, 6),
    'player 2': randint(1, 6),
    'player 3': randint(1, 6),
    'player 4': randint(1, 6)
}
print("=*" * 20)
print(f"{'DICE RAFFLE':^40}")
print("=*" * 20)
sleep(1)
for key, value in dice_rolls.items():
    print(f"The {key} took the number {value}".center(40))
    sleep(1)
print("=*" * 20)

player_order = sorted(dice_rolls.items(), key=itemgetter(1), reverse=True)

print(f"{'PLAYERS RANKING':^40}")
print("=*" * 20)
sleep(1)
for count, (key, value) in enumerate(player_order, start=1):
    print(f"The {count}º place: {key} with {value}".center(40))
    sleep(1)
print("=*" * 20)
