# Python Exercise 041 - Classifying Athletes
# The National Swimming Confederation needs a program that reads an athlete's birth year
# and shows their category, according to age:
# - Up to 9 years old: CHILDREN
# - Up to 14 years old: JUVENILE
# - Up to 19 years old: JUNIOR
# - Up to 25 years old: SENIOR
# - Over 25 years old: MASTER
import emoji
age = int(input("\033[1;36m Enter the age to find out which category the swimmer fits into: \033[m"))

if age <= 9:
    print(emoji.emojize("🏊" * 23, language='alias'))
    print(f"At age of {age}. You fit into the 'CHILDREN' category.")
    print(emoji.emojize("🏊" * 23, language='alias'))
elif age <= 14:
    print(emoji.emojize("🏊" * 25, language='alias'))
    print(f"At the age of {age}. You fit into the 'JUVENILE' category.")
    print(emoji.emojize("🏊" * 25, language='alias'))
elif age <= 19:
    print(emoji.emojize("🏊" * 24, language='alias'))
    print(f"At the age of {age}. You fit into the 'JUNIOR' category.")
    print(emoji.emojize("🏊" * 24, language='alias'))
elif age <= 25:
    print(emoji.emojize("🏊" * 24, language='alias'))
    print(f"At the age of {age}. You fit into the 'SENIOR' category.")
    print(emoji.emojize("🏊" * 24, language='alias'))
else:
    print(emoji.emojize("🏊" * 24, language='alias'))
    print(f"At the age of {age}. You fit into the 'MASTER' category.")
    print(emoji.emojize("🏊" * 24, language='alias'))