# Python Exercise 093 - Football Player Registration
# Create a program that manages the performance of a soccer player.
# The program will read the player's name and how many matches he played.
# Then you will read the amount of goals scored in each match.
# In the end, all of this will be kept in a dictionary, including the total goals scored during the championship.

register = {}
total_goals = []

register['Player name'] = str(
    input("Enter the player's name: ")).strip().title()
matches_played = int(input("Enter the amount of matches played: "))
for value in range(0, matches_played):
    total_goals.append(
        int(input(f"      Enter the quantity of goals in the match {value+1}: ")))
register['Goals per match'] = total_goals[:]
register['Total goals in the championship'] = sum(total_goals)
total_goals.clear()

print("=*" * 60)
print(register.items())
print("=*" * 60)
for key, value in register.items():
    print(f"{key}: {value}")
print("=*" * 60)

print("PERFORMANCE ANALYSIS".center(120))
print(
    f"The player {register['Player name']} played {matches_played} official matches.")
for count, goal in enumerate(register['Goals per match'], start=1):
    print(f"In the match number {count} scored {goal} goal(s).".center(30))
print(
    f"Total of {register['Total goals in the championship']} goals in the championship.")
