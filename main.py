import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")
scoreboard = Scoreboard()
car_speed = 0

game_is_on = True
counter = 0
while game_is_on:

    screen.update()
    time.sleep(0.1)
    if counter % 5 == 0:
        car_manager = CarManager()
        cars.append(car_manager)

    for car in cars:
        car.car_move(car_speed)
        if player.distance(car) < 25:
            player.player_reset()
            car_speed = 0
            scoreboard.dead_turtle()

    if player.ycor() == 280:
        player.player_reset()
        scoreboard.level_up()
        car_speed += 2
    counter += 1
