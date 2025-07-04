# Python Exercise 095 - Improving Dictionaries
# Enhance Challenge 93 so that it works with multiple players, including
# A detail viewing system of each player's performance.
total_goals = []
total_registers = []
while True:
    register = dict()
    register['Player name'] = str(
        input("Enter the player's name: ")).strip().title()
    matches_played = int(input("Enter the amount of matches played: "))
    for value in range(0, matches_played):
        total_goals.append(
            int(input(f"      Enter the quantity of goals in the match {value+1}: ")))
    register['Goals per match'] = total_goals[:]
    register['Total goals'] = sum(total_goals)
    total_goals.clear()
    total_registers.append(register.copy())

    while True:
        answer = str(input("Do you wish to continue? [Y/N] ")).strip().upper()
        if answer in ('Y', 'N'):
            break
        print("Invalid option. ", end='')
    if answer == 'N':
        break

print("=*" * 50)
print("PLAYER VIEW TABLE".center(100))
print("=*" * 50)
print(f"{'ID':<5} ", end='')
for key in register.keys():
    print(f"{key.upper():<40}", end='')
print()
print("-" * 100)
for key, value in enumerate(total_registers):
    print(f"{key:<5} ", end='')
    for data in value.values():
        print(f"{str(data):<40}", end='')
    print()

while True:
    ID = int(input("Enter the ID to know more of a player or (999 to QUIT): "))
    if ID == 999:
        print("=*" * 50)
        print("SYSTEM CLOSED.")
        break
    if ID >= len(total_registers):
        print(f"ERROR! There's no player with ID {ID}.")
    else:
        print("=*" * 50)
        print("PERFORMANCE ANALYSIS".center(100))
        print("=*" * 50)
        print(
            f"The player {total_registers[ID]['Player name']} played {matches_played} official matches.")
        for count, goal in enumerate(total_registers[ID]['Goals per match'], start=1):
            print(
                f"In the macth number {count} scored {goal} goal(s).".center(30))
        print(
            f"Total of {total_registers[ID]['Total goals']} goals in the championship.")
