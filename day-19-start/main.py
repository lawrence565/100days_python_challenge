from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 500)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

for i in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=(-100 + 50 * i))
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if turtle.pencolor() == user_bet.lower():
                print(f"You win!!!, The {winner} turtle is the winner")
            else:
                print(f"Tou lost, , The {winner} turtle is the winner")

        rand_dis = random.randint(0, 10)
        turtle.forward(rand_dis)

screen.exitonclick()
