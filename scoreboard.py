from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 160)
        self.color("white")
        self.update_score()
    
    
    def update_score(self):
        self.clear()
        self.write(
            f"{self.score_l} : {self.score_r}",
            False,
            align="center",
            font=("Verdana", 20, "normal"),
        )