from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(-250, 250)
        self.hideturtle()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self, level):
        self.clear()
        self.level = level
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
