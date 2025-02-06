from turtle import Turtle,Screen
import turtle
import random
import colorgram

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color

# def draw():
#     total_distance = 0
#     for _ in range(num_circles):
#         # tim.pendown()
#         tim.fillcolor(random.choice(all_colors))
#         tim.begin_fill()
#         tim.circle(radius)
#         tim.end_fill()
#         # tim.penup()
#         tim.pencolor()
#         tim.forward(diameter + space)
#         total_distance += diameter + space
#     return total_distance

# rgb_colors = []
# colors = colorgram.extract("image.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
def draw(dots_number):
    total_path = 0
    for _ in range(dots_number):
        tim.dot(diameter,random.choice(all_colors))
        tim.forward(space)
        total_path += space
    return total_path

def reset(space_returned):
    """Return to the beginning of the line and change the column"""
    tim.backward(space_returned)
    tim.left(90)
    tim.forward( space)
    tim.right(90)


all_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
              (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]



turtle.colormode(255)
tim = Turtle()
screen = Screen()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
# tim.pencolor("white")
tim.teleport(-380,-350)

num_lines = 10
num_circles = 10
space = 50
diameter = 20
radius = diameter/2

for _ in range(num_lines):
    return_distance = draw(num_circles)
    reset(return_distance)


screen.exitonclick()


