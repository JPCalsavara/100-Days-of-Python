from turtle import Turtle
ALIGN = "center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"Score:{self.points}",align=ALIGN, font=FONT)

    def earn_point(self):
        self.points += 1
        self.clear()
        self.write(f"Score:{self.points}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)