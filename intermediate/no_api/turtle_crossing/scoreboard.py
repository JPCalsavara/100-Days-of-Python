from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Level: {self.score}",align="center", font=("Courier",25,"normal"))

    def add_score(self):
        self.score +=1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,50)
        self.write(f"Game Over\nLevel: {self.score}",align="center", font=("Courier",25,"normal"))
