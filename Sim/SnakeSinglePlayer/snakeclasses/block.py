from kivy.uix.widget import Widget
from kivy.properties import ListProperty

from snakeclasses.config import Config

class Block(Widget):

    color = ListProperty([1., 1., 1.])

    def __init__(self, printing, coorx, coory):
        super().__init__()
        self.coorx = coorx
        self.coory = coory
        width = Config().CELL_WIDTH
        height = Config().CELL_HEIGHT
        self.size = (width-6, height-6)
        self.pos = (Config().ZERO_X + width*coorx + 3,Config().ZERO_Y + height*coory + 3)
        self.color = (0.2, 1.0, 0.2)
        if printing == 1:
            print("block created with positions: ", width*coorx, " and ", height*coory, "width: ", width, "and height: ", height)


    def change_location(self, printing, coorx, coory):
        self.coorx = coorx
        self.coory = coory
        width = Config().CELL_WIDTH
        height = Config().CELL_HEIGHT
        self.pos = (Config().ZERO_X + width*coorx + 3,Config().ZERO_Y + height*coory + 3)
        if printing == 1:
            print("block changed to positions: ", width*coorx, " and ", height*coory, "width: ", width, "and height: ", height)
