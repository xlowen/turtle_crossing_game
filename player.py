from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.setpos(STARTING_POSITION)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def player_reset(self):
        self.setpos(STARTING_POSITION)

    def game_reset(self):
        self.player_reset()
