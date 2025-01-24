from turtle import Turtle
ALIGN = "center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.points} High Score:{self.high_score}",align=ALIGN, font=FONT)

    def earn_point(self):
        self.points += 1
        self.update_score()

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.points = 0
        self.update_score()
