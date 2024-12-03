from turtle import Screen, Turtle
from ball import Ball
from scoreboard import Scoreboard
import pedal, time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_pedal = pedal.RightPedal()
left_pedal = pedal.LeftPedal()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_pedal.up, "Up")
screen.onkeypress(right_pedal.down, "Down")
screen.onkeypress(left_pedal.up, "w")
screen.onkeypress(left_pedal.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    # Detect collision with Ceiling and Floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with Pedal
    if (320 < ball.xcor() < 350 and ball.distance(right_pedal) < 50) or (-350 < ball.xcor() < -320 and ball.distance(left_pedal) < 50):
        ball.acceleration()
        ball.bounce_x()

    # Detect passing the barrier
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.refresh()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.refresh()






screen.exitonclick()