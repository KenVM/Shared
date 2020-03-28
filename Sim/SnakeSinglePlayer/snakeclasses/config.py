from kivy.core.window import Window


class Config():


    GRID_WIDTH = 9
    GRID_HEIGHT = 8
    GAMESCREEN_WIDTH = 0.9 #90 percent of screen for the snake window
    GAMESCREEN_HEIGHT = 0.8 #80 percent of screen for the snake window



    window_size = Window.size
    CELL_WIDTH = (GAMESCREEN_WIDTH * window_size[0]) / GRID_WIDTH
    CELL_HEIGHT = (GAMESCREEN_HEIGHT * window_size[1]) / GRID_HEIGHT

    X_PERCENTAGE = (1 - GAMESCREEN_WIDTH) / 2
    Y_PERCENTAGE = (0.9 - GAMESCREEN_HEIGHT) / 2

    ZERO_X = X_PERCENTAGE * window_size[0]
    ZERO_Y = Y_PERCENTAGE * window_size[1]

    ONE_X = (1 - X_PERCENTAGE) * window_size[0]
    ONE_Y = (0.9 - Y_PERCENTAGE) * window_size[1]
