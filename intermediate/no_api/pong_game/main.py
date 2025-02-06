from turtle import Turtle,Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import time


player1_start_position = (-350,0)
player2_start_position = (350,0)

receiver_player = 0


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
paddle1 = Paddle(player1_start_position)
paddle2 = Paddle(player2_start_position)

screen.listen()
screen.onkey(fun=paddle1.go_up,key="w")
screen.onkey(paddle1.go_down, "s")
screen.onkey(paddle2.go_up,"Up")
screen.onkey(paddle2.go_down, "Down")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    #Detect collision with the paddle
    if ball.distance(paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle1) < 50 and ball.xcor() < -320  :
        ball.bounce_paddle()

    #Reset the ball and counting points
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.p1_point()

    elif ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.p2_point()




screen.exitonclick()