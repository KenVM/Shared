

from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen

from screens.screenmanagement import ScreenManagement
from screens.snakescreen import SnakeScreen
from screens.appscreen import AppScreen

from kivymd.app import MDApp

import time


class ClientApp(MDApp):
    print("Client app initialization")
    Builder.load_file("main.kv")

    def build(self):

        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        self.theme_cls.primary_hue = "A700"  # "500", "A700"   hoog is dieper/donkere kleur

        manager = ScreenManagement.getInstance()
        initialize_screen = Screen(name="init_screen") #just used for init

        screen_snake = SnakeScreen(name="screen_snake")
        screen_start = AppScreen(name="screen_app")

        windows = [initialize_screen, screen_start, screen_snake]
        for window in windows:
             manager.add_widget(window)

        manager.current = "screen_app"
        time.sleep(0.5)

        return manager

print("main program")
ClientApp().run()
