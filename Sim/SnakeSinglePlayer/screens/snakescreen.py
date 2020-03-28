from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty

from screens.screenmanagement import ScreenManagement
from snakeclasses.block import Block
from snakeclasses.snakegame import SnakeGame
from snakeclasses.config import Config

class SnakeScreen(Screen):


    game_running = False
    color = ListProperty([1., 1., 1.])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initialize_snakegame()
        self.game_running == True
        
    def on_enter(self, *args):
        if self.game_running == False:
            self.initialize_snakegame()

        self.snakegame.run_game()

    # def on_leave(self, *args):
    #     print("leaving snake")

    def initialize_snakegame(self):
        self.game_running = True
        self.snakegame = SnakeGame()
        self.add_widget(self.snakegame)

    def terminate_snakegame(self):
        self.snakegame.pause_game()
        self.game_running = False
        self.remove_widget(self.snakegame)

    # method called by pause button
    def pause_game(self,dt):
        self.snakegame.pause_game()
        manager = ScreenManagement.getInstance()
        self.manager.current = "screen_app"

    # method called by quit button
    def quit_game(self,dt):
        self.terminate_snakegame()
        manager = ScreenManagement.getInstance()
        self.manager.current = "screen_app"
