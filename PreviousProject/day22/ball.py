from turtle import Turtle


class Ball(Turtle):
    def __init__(self, ball_xcor, ball_ycor):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=0.8, stretch_len=0.8)
        self.goto(ball_xcor, ball_ycor)
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def reset_postion(self):
        self.goto(0, 0)
        self.bounce_x()

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
