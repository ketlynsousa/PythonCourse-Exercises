# Python Exercise 101 - Voting Functions
# Create a program that has a function called vote() that will receive as a parameter the year of birth of a
# person, returning a literal value indicating whether a person's vote is PROHIBITED, OPTIONAL, and MANDATORY in the elections.
def vote(year):
    from datetime import date
    age = date.today().year - year
    if age < 16:
        return print(f'At {age} years old the vote is PROHIBITED.')
    elif 16 <= age < 18:
        return print(f'At {age} years old the vote is OPTIONAL.')
    elif 18 <= age <= 70:
        return print(f'At {age} years old the vote is MANDATORY.')
    else:
        return print(f'At {age} years old the vote is OPTIONAL.')


print("=*" * 25)
print("SYSTEM TO KNOW THE ELECTORAL SITUATION.".center(50))
print("=*" * 25)
year_birth = int(input("Enter your year of birth: "))
vote(year_birth)
