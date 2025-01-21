from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"Score:{self.points}",align="center", font=("Arial",24,"normal"))

    def earn_point(self):
        self.points += 1
        self.clear()
        self.write(f"Score:{self.points}", align="center", font=("Arial",24,"normal"))