from turtle import Turtle,Screen
import turtle
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def draw():
    for _ in range(num_circles):
        tim.pendown()
        tim.begin_fill()
        tim.circle(radius)
        tim.end_fill()
        tim.penup()
        tim.pencolor(random_color())
        tim.forward(diameter + space)


def reset():
    """Return to the beginning of the line and change the column"""
    total_space = num_circles * (diameter+space)
    tim.backward()
    tim.left(90)
    tim.forward(diameter + space)
    tim.right(90)


turtle.colormode(255)
tim = Turtle()
screen = Screen()
tim.penup()
tim.teleport(-300,-300)

num_lines = 8
num_circles = 8
space = 20
diameter = 80
radius = diameter/2

for _ in range(num_lines):
    draw()
    reset()


screen.exitonclick()


