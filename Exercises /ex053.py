# Python Exercise 053 - Palindrome Detector
# Create a program that reads any sentence and tells you if it is a palindrome, disregarding spaces.
# Examples: Taco cat, Dennis sinned, No lemons no melon
print("Let's find out if your sentence is a palindrome!")
phrase = str(input("Type a sentence: ")).strip().upper().replace(" ", "")
inverted_sentence = phrase[::-1]

if phrase == inverted_sentence:
    print(f"The inverse of the {phrase} is {inverted_sentence.upper()}. The phrase is a palindrome.")
else:
    print(f"The inverse of the {phrase} is {inverted_sentence.upper()}. The phrase is NOT a palindrome.")
