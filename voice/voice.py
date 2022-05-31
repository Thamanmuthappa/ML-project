import os
import platform

from kivy.core.window import Window
from kivymd.app import MDApp

from libs.uix.baseclass.root import Root

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

class voice(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(voice, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "voice"

        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.primary_hue = "100"

        self.theme_cls.accent_palette = "DeepPurple"
        self.theme_cls.accent_hue = "700"

        self.theme_cls.theme_style = "Light"

    def build(self):
        return Root()

    
            
            
            
