# TODO 1: Create the screen
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
RIGHT_POSITION = (350, 0)
LEFT_POSITION = (-350, 0)


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# TODO 2: Create and move a paddle
r_paddle = Paddle(RIGHT_POSITION)
# TODO 3: Create another paddle
l_paddle = Paddle(LEFT_POSITION)
# TODO 4: Create the ball and make it move
ball = Ball()
# TODO 8: Keep score
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    # control the speed of the ball, 0.01 is faster than 0.1
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO 5: Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # TODO 6: Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO 7: Detect when paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()







