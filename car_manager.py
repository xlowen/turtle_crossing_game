from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
# move_increment = 0


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLORS[random.randint(0, 5)])
        self.shape("square")
        self.setpos(300, random.randint(-200, 200))
        self.shapesize(1.0, 2.0, 0)
        self.setheading(180)

    def car_move(self, move_increment):
        self.forward(STARTING_MOVE_DISTANCE + move_increment)