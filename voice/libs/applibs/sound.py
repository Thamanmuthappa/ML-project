import pygame
import random
from assets.song.song import *
from libs.applibs.speak import speak

def openSound():
    '''
    Play sound when run voice
    '''
    pygame.mixer.init()
    pygame.mixer.music.load("assets\sound\open.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def sing():
    '''
    Play a song
    '''
    while pygame.mixer.music.get_busy() == True:
        continue
    speak("Let's listen this song until the end!")
    pygame.mixer.init()
    pygame.mixer.music.load(random.choice(play_list))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    