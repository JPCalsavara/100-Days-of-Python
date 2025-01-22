from turtle import Turtle,Screen

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.p1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.p2_score, align="center", font=("Courier", 80, "normal"))

    def p1_point(self):
        self.p1_score+=1
        self.update_score()

    def p2_point(self):
        self.p2_score+=1
        self.update_score()