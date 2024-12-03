import random
import turtle as t

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
circle_amount = 60
radius = 100

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_graph):
    for _ in range( 360 // size_of_graph):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + size_of_graph)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()