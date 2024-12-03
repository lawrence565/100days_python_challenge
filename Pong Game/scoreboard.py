from turtle import Turtle

FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        # Write the scores of both side
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
