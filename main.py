import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
scoreboard.game_over()
player = Player()

screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()
game_is_on = True
while game_is_on:
    car_manager.generate_car()
    car_manager.move()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()