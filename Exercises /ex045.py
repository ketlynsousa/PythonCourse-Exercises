# Python Exercise 045 - GAME: Rock, Paper, Scissors
# Create a program that makes the computer play Rock, Paper, Scissors with you.

import emoji
from random import choice
from time import sleep

#function to emojis display
def use_emoji(name: str) -> str:
    alias_formatted = f":{name.strip()}:"
    return emoji.emojize(alias_formatted, language='alias')

#dictionary for emojis
emojis = {'rock': use_emoji('moyai'),
          'paper': use_emoji('rolled-up_newspaper'),
          'scissor': use_emoji('scissors'),
          'controller': use_emoji('video_game'),
          'sunglasses': use_emoji('sunglasses'),
          'thinking': use_emoji('thinking_face')}
#dictonary for colors
colors = {'red': '\033[31m',
          'green': '\033[32m',
          'yellow': '\033[33m',
          'purple': '\033[35m',
          'cyan': '\033[36m',
          'clean': '\033[m'}

game_list = ['paper', 'rock', 'scissors']
#Introduction to the game
print(f"{emojis['controller']}" * 20)
print(f"{colors['purple']}Let's play the rock, paper, scissor game.{colors['clean']}")
print(f"{emojis['controller']}" * 20)
sleep(2)

#Computer option section
computer = choice(game_list)

#Player option section
for word in ["LET'S GO!!!", "Rock", "Paper", "Scissors"]:
    print(word)
    sleep(0.9)
print(f"{emojis['paper']} {emojis['rock']} {emojis['scissor']}")
player = str(input("Write your choice: ")).lower().strip()

#Invalid choice option section
if player not in game_list:
    print(f"{colors['red']}Invalid choice, please try again. Only Rock, Paper, and Scissors are allowed.{colors['clean']}")


print(f"Let's see...")
print(f"{emojis['thinking']}" * 5)
sleep(2)


#Win or Lost conditions for the game
print(f"\nYou chose {player.title()} and I chose {computer.title()}.")
if computer == player:
    print(f"{colors['yellow']}We TIED!!!{colors['clean']}")

elif player == 'rock' and computer == 'scissors':
    print(f"{colors['green']}You WON!!!{colors['clean']}")

elif player == 'scissors' and computer == 'paper':
    print(f"{colors['green']}You WON!!!{colors['clean']}")

elif player == 'paper' and computer == 'rock':
    print(f"{colors['green']}You WON!!!{colors['clean']}")

else:
    print(f"{colors['red']}You LOST!!!{colors['clean']}"
          f"{colors['cyan']} I WON!!!{colors['clean']} {emojis['sunglasses']}{emojis['sunglasses']}{emojis['sunglasses']}")
