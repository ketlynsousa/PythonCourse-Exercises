# Python Exercise 077 - Counting vowels in a tuple
# Create a program that has a tuple with several words.
# After that, you must show, for each word, what vowels they are in the world.
words = ('learn', 'programmer', 'language', 'python', 'course', 'study', 'practice', 'work', 'market', 'developer', 'future')

for word in words:
    print(f"\nIn the word {word.upper()} there are the vowels ", end='')
    for letter in word:
        if letter.upper() in "AEIOU":
            print(f"\033[34m{letter.upper()}\033[m", end=' ')
