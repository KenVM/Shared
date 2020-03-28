from random import randint

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivymd.toast import toast

from snakeclasses.block import Block
from snakeclasses.player import Player
from snakeclasses.config import Config
from screens.screenmanagement import ScreenManagement
from globalfunctions.collision import collision


class SnakeGame(Widget):

    snakegame_property = ObjectProperty(None)
    score_label = ObjectProperty(None)
    pos_hintx = NumericProperty(0.1)
    pos_hinty = NumericProperty(0.1)
    color = ListProperty([1., 1., 1.])


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("init SnakeGame")

        self.snakegame_property.size_hint = [Config().GAMESCREEN_WIDTH , Config().GAMESCREEN_HEIGHT]
        self.snakegame_property.pos_hint = {'x': Config().X_PERCENTAGE, 'y': Config().Y_PERCENTAGE }

        self.highscore = 0

        player_init_list = [[1,1],[1,0],[0,0]]
        self.player_one = Player(False, player_init_list)
        self.add_widget(self.player_one)

        self.apple = Block(False, 4, 4)
        self.add_widget(self.apple)
        self.apple.color = (0.4, 1, 1)

    def run_game(self):
        print("game is running")
        manager = ScreenManagement.getInstance()
        Clock.schedule_interval(self.update_function, float(manager.speed))  #0 means every frame / 1 is every second / 0.001 every ms

    def pause_game(self):
        print("game is paused")
        Clock.unschedule(self.update_function)
        if self.player_one.score > self.highscore:
            #print("NEW HIGHSCORE ACHIEVED :" , self.player.score)
            self.highscore = self.player_one.score

    def update_function(self, dt):
        print("update")
        self.player_one.update()
        self.parent.score_label.text = "score: " + str(self.player_one.score)

        if collision(self.player_one.block_array[:], self.apple):
            self.player_one.add_block(False)
            self.apple.change_location(False, randint(0,Config.GRID_WIDTH-1), randint(0,Config.GRID_HEIGHT-1))
            self.player_one.score += 1
            print(self.player_one.score)

        if self.player_one.block_array[0].pos[0] < Config.ZERO_X or self.player_one.block_array[0].pos[1] < Config.ZERO_Y or self.player_one.block_array[0].pos[0] > Config.ONE_X or self.player_one.block_array[0].pos[1] > Config.ONE_Y:
            toast("GAME OVER")
            self.parent.quit_game(dt)

        if collision(self.player_one.block_array[0], self.player_one.block_array[1:]):
            toast("GAME OVER")
            self.parent.quit_game(dt)


    #triggered when screen is touched, will determine direction of player
    def on_touch_up(self, touch):
        dx = touch.x - touch.opos[0]
        dy = touch.y - touch.opos[1]
        #print(dx, dy)
        direction = self.player_one.direction

        if direction == "right" or direction == "left" :
            if dy > 0:
                self.player_one.direction = "up"
            else:
                self.player_one.direction = "down"
        if direction == "up" or direction == "down" :
            if dx > 0:
                self.player_one.direction = "right"
            else:
                self.player_one.direction = "left"

        print(self.player_one.direction)
