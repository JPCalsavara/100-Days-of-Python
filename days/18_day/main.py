import random
import turtle
from turtle import Turtle, Screen

colours = ["cornflower blue", "spring green","sandy brown","deep pink","yellow","red"]

turtle.colormode(255)
tim = Turtle()
# tim.shape("turtle")
# tim.color("blue")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# for _ in range(30):
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()


# sides = 3
# while sides < 11:
#     for _ in range(sides):
#         tim.forward(100)
#         angle = 360 / sides
#         tim.right(angle)
#     sides += 1
#     color = random.choice(colours)
#     tim.pencolor(color)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

# tim.pensize(20)
# tim.speed(10)
# for _ in range(100):
#     direction = random.randint(1,4)
#     tim.right(90 * direction)
#     tim.forward(40)
#     tim.pencolor(random_color())

num_circle = 200
tim.speed("fastest")
for _ in range(num_circle):
    tim.circle(100)
    tim.right(360/num_circle)
    tim.pencolor(random_color())

screen = Screen()
screen.exitonclick()