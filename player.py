from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.y_position = self.ycor()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        not_finish = True
        self.forward(MOVE_DISTANCE)
        self.y_position = self.ycor()

    def reset(self):
        self.goto(STARTING_POSITION)
        self.y_position = self.ycor()
        self.setheading(90)



