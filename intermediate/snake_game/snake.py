import time
from turtle import Turtle,Screen

STARTING_POSITION = [(0,-20),(-20,-20),(-40,-20)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.inicialize()
        self.head = self.snake_body[0]

    def inicialize(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
            new_block = Turtle(shape="square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(position)
            self.snake_body.append(new_block)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def constant_moving(self):
        for index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[index - 1].xcor()
            new_y = self.snake_body[index - 1].ycor()
            self.snake_body[index].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)