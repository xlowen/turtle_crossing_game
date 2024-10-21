from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(COLORS[random.randint(0, 5)])
        self.shape("square")
        self.setpos(300, random.randint(-200, 200))
        self.shapesize(1.0, 2.0, 0)
        self.setheading(180)

    def car_move(self):
        self.forward(STARTING_MOVE_DISTANCE)