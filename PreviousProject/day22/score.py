from turtle import Turtle


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.x = x
        self.y = y
        self.score = 0
        self.goto(x, y)


    def print_score(self, score_count):
        self.clear()
        self.write(f"{score_count}",font=("Courier",80,"normal"))
