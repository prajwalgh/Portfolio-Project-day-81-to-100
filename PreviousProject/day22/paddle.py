from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_xcor, paddle_ycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(paddle_xcor, paddle_ycor)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def upw(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def downs(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
