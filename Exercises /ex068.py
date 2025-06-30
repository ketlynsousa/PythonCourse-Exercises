# Python Exercise 068 - Odd or Even Game
# Make a program that you play odd or even with the computer. The game will only be interrupted when the player loses,
# showing the total number of consecutive wins he achieved in the end of the game.

from random import randint
cont = 0
#introduction to game
print("LET'S PLAY ODD OR EVEN GAME.")

while True:
    #computer choice
    computer_choice = randint(0, 10)

    #player choice and errors validation
    odd_even_option = str(input("Type if chose ODD or EVEN [O/E]: ")).strip().upper()[0]
    while odd_even_option not in ("E", "O"):
        print("Invalid option. Try again")
        odd_even_option = str(input("Type if chose ODD or EVEN [O/E]: ")).strip().upper()[0]

    player_choice = int(input("Enter a number from (0 to 10) to play: "))
    while player_choice not in range(0, 11):
        print("Invalid option. Try again")
        player_choice = int(input("Enter a number from (0 to 10) to play: "))

    #add calculation to define the winner
    add = computer_choice + player_choice

    #contions to win or lose
    if odd_even_option == 'E':
        print(
            f"\nYou played EVEN with number {player_choice} and the computer played {computer_choice}.\nThe sum was {add}.")
    if odd_even_option == 'O':
        print(f"\nYou played ODD with number {player_choice} and the computer played {computer_choice}.\nThe sum was {add}.")
    if odd_even_option == 'E' and add % 2 == 0:
        print(f"YOU WON!!!")
        print("LET'S PLAY AGAIN...")
        print("=" * 60)
        cont += 1
    elif odd_even_option == 'O' and add % 2 != 0:
        print("YOU WON!!!")
        print("LET'S PLAY AGAIN...")
        print("=" * 60)
        cont += 1
    else:
        print("GAMER OVER!!!")
        print("=" * 60)
        print(f"You won {cont} times.")
        break
