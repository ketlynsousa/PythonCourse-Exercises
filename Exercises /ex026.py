# Python Exercise 026 - First and last occurrence of a string
# Write a program that reads a sentence from the keyboard and shows:
# - How many times the letter 'A' appears
# - In which position it appears the first time
# - In which position it appears the last time

sentence = str(input("Write a sentence: ")).strip().upper()
print(f"The letter 'A' appears {sentence.count('A')} times.")
print(f"The first letter 'A' appears in position {sentence.find('A') + 1}.")
print(f"The last letter 'A' appears in position {sentence.rfind('A') + 1}")
