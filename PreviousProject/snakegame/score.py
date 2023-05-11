from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.data = 0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.goto(0, 250)
        self.penup()b
        self.hideturtle()
        self.color("white")
        self.write(f"score is {self.data}  high score is { self.high_score}", move=False, align="center", font=(10))

    def print_score(self):
        self.clear()
        self.write(f"score is {self.data} high score is { self.high_score} ", move=False, align="center", font=(10))
    def reset(self):
        if self.data>self.high_score:
            self.high_score=self.data
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.print_score()
    def increse_score(self):
        self.data += 1
        self.print_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER ", move=False, align="center", font=(10))