from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.direction = "right"

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.direction != "down":
            self.segments[0].setheading(90)
        self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.segments[0].setheading(270)
        self.direction = "down"

    def right(self):
        if self.direction != "left":
            self.segments[0].setheading(0)
        self.direction = "right"

    def left(self):
        if self.direction != "right":
            self.segments[0].setheading(180)
        self.direction = "left"