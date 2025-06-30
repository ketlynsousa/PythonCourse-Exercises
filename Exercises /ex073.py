# Python Exercise 073 - Tuples with Soccer Teams
# Create a tuple filled with the top 20 teams in the Brazilian Soccer Championship Table,
# in order of placement. Then show:
# a) The top 5 teams.
# b) The last 4 teams.
# c) Teams in alphabetical order.
# d) What position is 'São Paulo' team in.
football_championship = ('Flamengo', 'Cruzeiro', 'Red Bull Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG', 'Botafogo', 'Mirassol',
                      'Corinthians', 'Grêmio', 'Ceará', 'Vasco', 'São Paulo', 'Santos', 'Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')

print('=*' * 60)
print(f"\033[1;34m{"Analysis of the teams in the Brazilian Football Championship Series A":^120}\033[m")
print('=*' * 60)

print("The top five in the championship:")
for count in range(0, 5):
    print(f"\033[32m{count + 1}º place is {football_championship[count]}.\033[m")
print('=*' * 60)

print("The last 4 placed in the championship:")
for count in range(-4, 0):
    print(f"\033[31m{20 + count + 1}º place is {football_championship[count]}.\033[m")
print('=*' * 60)

print("List of championship teams organized in alphabetical order: ")
for team in sorted(football_championship):
    print(f" - {team}")
print('=*' * 60)

print("The position of the São Paulo team:")
print(f"\033[33mSão Paulo is in {football_championship.index('São Paulo') + 1}º position in the championship table.\033[m")
