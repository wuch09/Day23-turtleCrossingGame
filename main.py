import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()

game_is_on = True
speed_factor = 0.5
speed = 0.1
while game_is_on:
    car_manager.generate_car()
    game_is_on = car_manager.move(player)
    if player.y_position > 280:
        speed = speed * speed_factor
        player.reset()
        scoreboard.level_up()
        scoreboard.update_level()
    time.sleep(speed)

    screen.update()
scoreboard.game_over()
screen.exitonclick()