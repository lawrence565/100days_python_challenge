from turtle import Turtle
import random

class Ball(Turtle):
    x_direction = random.choice((-10, 10))
    y_direction = random.choice((-10, 10))
    speed = 0.1

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)

    def refresh(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.bounce_x()

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1

    def acceleration(self):
        self.speed *= 0.95