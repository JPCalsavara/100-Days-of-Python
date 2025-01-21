import time
from turtle import Turtle,Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.start_position = 0
        self.inicialize()
        self.head = self.snake_body[0]

    def inicialize(self):
        for _ in range(3):
            new_block = Turtle(shape="square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(x=self.start_position, y=-20)
            self.snake_body.append(new_block)
            self.start_position -= MOVE_DISTANCE
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