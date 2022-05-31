from kivymd.uix.screen import MDScreen
#import rule
from rule import *

class HomeScreen(MDScreen):
    def __init__(self) -> None:
        super().__init__()
    def talk(self):
        robot()
