from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from screens.screenmanagement import ScreenManagement

class AppScreen(Screen):

    highscore_label = ObjectProperty(None)
    speed_slider = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print("init screen app")

    def on_enter(self, *args):
        # print("entering app screen")
        manager = ScreenManagement.getInstance()

        self.highscore_label.text = "Current highscore is " + str(self.manager.get_screen("screen_snake").snakegame.highscore)

    def start_snake(self, dt):
        manager = ScreenManagement.getInstance()
        manager.speed = self.speed_slider.value/10
        print(manager.speed)
        manager.current = "screen_snake"
