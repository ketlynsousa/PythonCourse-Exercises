# Python Exercise 046 - Countdown
# Write a program that displays a countdown on the screen for fireworks to go off, going from 10 to 0, with 1 second pause between them.
from time import sleep
import emoji
print('=' * 35)
print("COUNTDOWN FOR FIREWORKS".center(35))
print('=' * 35)
for c in range(10, -1 , -1):
    print(c)
    sleep(1)
print("BOOM! BOOM! WHIZZ! POWPOW!")
print(emoji.emojize("🎆" * 12, language='alias'))
