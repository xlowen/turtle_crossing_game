from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    level = 1
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.setpos(-200, 260)
        self.write(f"Level: {self.level}", False, "center", FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "center", FONT)