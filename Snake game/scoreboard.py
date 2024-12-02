from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Scores: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over, Your score is {self.score}!", align="center", font=FONT)


    def update_scores(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

