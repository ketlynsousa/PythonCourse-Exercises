# Python Exercise 021 - Playing an MP3
# Write a Python program that opens and plays the audio from an MP3 file.
import pygame
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play(0)
input()
pygame.mixer_music.stop()
input()
