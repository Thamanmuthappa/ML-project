import pyjokes
from libs.applibs.speak import speak
import random
import pygame
from assets.laugh_sound.laugh import *

def get_joke():
    joke = pyjokes.get_joke(language='en',category='all')
    speak(joke)

    # haha sound
    
    pygame.mixer.init()
    pygame.mixer.music.load(random.choice(laugh_list))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
