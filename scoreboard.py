from turtle import Turtle
LEVEL_FONT = ("Courier", 16, "normal")
PROMPT_POSITION = (-240, 260)
LEVEL_POSITION = (-180, 260)
GAME_OVER_POSITION = (0, 0)
GAME_OVER_FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(PROMPT_POSITION)
        self.write("Level: ", align="center", font=LEVEL_FONT)
        self.update_level()

    def level_up(self):
        self.level +=1

    def update_level(self):
        self.clear()
        self.goto(PROMPT_POSITION)
        self.write("Level: ", align="center", font=LEVEL_FONT)
        self.goto(LEVEL_POSITION)
        self.write(self.level, align="center", font=LEVEL_FONT)

    def game_over(self):
        self.goto(GAME_OVER_POSITION)
        self.write("Game Over", align="center", font=GAME_OVER_FONT)

