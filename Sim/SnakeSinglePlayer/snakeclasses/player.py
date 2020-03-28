from random import randint

from kivy.properties import ListProperty
from kivy.uix.widget import Widget

from snakeclasses.block import Block
from snakeclasses.config import Config

class Player(Widget):

    def __init__(self, printing, init_list):
        super().__init__()
        if printing == 1:
            print("creating player with folowing list: ", init_list)

        self.score = len(init_list)
        self.block_array = []

        for xy_position in init_list:
            blck = Block(printing, xy_position[0], xy_position[1])
            self.add_widget(blck)
            self.block_array.append(blck)

        self.direction = "up"

    def update(self):
        color = ListProperty([1., 1., 1.])

        print("updating a player")
        x_update = 0
        y_update = 0
        if self.direction == "right":
            x_update = Config.CELL_WIDTH
        elif self.direction == "up":
            y_update = Config.CELL_HEIGHT
        elif self.direction == "down":
            y_update = -Config.CELL_HEIGHT
        elif self.direction == "left":
            x_update = -Config.CELL_WIDTH

        #change position last block to position first block + update
        self.block_array[-1].pos[0] = self.block_array[0].pos[0]+x_update
        self.block_array[-1].pos[1] = self.block_array[0].pos[1]+y_update

        #put last block in the front of the raw
        self.block_array = self.block_array[-1:] + self.block_array[:-1]
        self.block_array[0].color = (0.2, 1.0, 0.2)

    def add_block(self, printing):
        blck = Block(printing, 0, 0)
        blck.pos = [self.block_array[-1].pos[0], self.block_array[-1].pos[1]]
        self.add_widget(blck)
        self.block_array.append(blck)
