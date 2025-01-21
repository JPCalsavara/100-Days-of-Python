import random
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red","orange","yellow","green","blue","purple"]
turtles =[]
start_position = -70
is_race_on = True

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230,y=start_position)
    turtles.append(new_turtle)
    start_position += 30

while is_race_on:
    if turtle.xcor() > 230:
        is_race_on = False
        winning_color = turtle.pencolor()
        if winning_color == user_bet:
            print(f"You've won! The {winning_color} turtle is the winner!")
        else:
            print(f"You lose. The {winning_color} turtle is the winner!")
    for turtle in turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
