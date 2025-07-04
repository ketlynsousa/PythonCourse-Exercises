# Python Exercise 088 - Predictions for Mega Sena
# Write a program that helps a TheLotter player create predictions.
# The program will ask how many games will be generated and will draw 6 numbers between 1 and 60 for each game.
from random import randint
from time import sleep
temporary_list = []
games_list = []

print("=*" * 30)
print(f"{'THELOTTER GAMES':^60}")
print("=*" * 30)
qtt_games = int(input("How many games would you like to raffle? "))
total_games = 1
while total_games <= qtt_games:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in temporary_list:
            temporary_list.append(num)
            count += 1
            if count == 6:
                break

    temporary_list.sort()
    games_list.append(temporary_list[:])
    temporary_list.clear()
    total_games += 1
print("=*" * 5, f"RAFFLE OF {qtt_games} GAMES", "=*" * 5)
for i, play in enumerate(games_list):
    print(f"Game {i + 1}: {play}")
    sleep(1)
print("=*" * 5, f"<   GOOD LUCK!   >", "=*" * 5)
