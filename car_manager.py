import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_queue = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(340, random.randint(-250, 250))
            self.car_queue.append(new_car)

    def move(self, player):
        for car in self.car_queue:
            car.backward(self.car_speed)
            if car.xcor() < -340:
                self.car_queue.remove(car)
            if car.distance(player) < 20:
                return False
        return True

    def level_up(self):
        self.car_speed += MOVE_INCREMENT









