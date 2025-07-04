# Python Exercise 103 - Player Profile
# Write a program that has a function called profile(), which receives two additional clauses:
# the name of a player and how many goals he scored. The program should be able to show the player profile,
# even if some data has not been provided
def profile(name='<unknown>', goals=0):
    print(
        f"The player {name.title()} scored {goals} goal(s) in the tournament.")


print("=*" * 25)
print("PLAYER PERFORMANCE RECORD".center(50))
print("=*" * 25)
player = str(input("Player's name: "))
total_goals = str(input("Amount of goal(s) : "))
if total_goals.strip() == '':
    total_goals = 0
if player.strip() == '':
    profile(gols=total_goals)
else:
    profile(player, total_goals)
