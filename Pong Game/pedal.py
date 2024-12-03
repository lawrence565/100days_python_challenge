from turtle import Turtle

class Pedal(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()


    def up(self):
        new_y = self.ycor() + 20
        x = self.xcor()
        self.goto(x, new_y)

    def down(self):
        new_y = self.ycor() - 20
        x = self.xcor()
        self.goto(x, new_y)

class RightPedal(Pedal):

    def __init__(self):
        super().__init__()
        self.goto(350, 0)
        print("Coordinate", self.xcor(), self.ycor())


class LeftPedal(Pedal):

    def __init__(self):
        super().__init__()
        self.goto(-350, 0)
        print("Coordinate", self.xcor(), self.ycor())