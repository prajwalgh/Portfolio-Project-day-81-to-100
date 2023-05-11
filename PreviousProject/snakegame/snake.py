from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_BY = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.Create_snake()
        self.head = self.segment[0]

    def Create_snake(self):
        for pos in STARTING_POSITION:
            self.add_seg(pos)

    def add_seg(self, pos):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(pos)
        self.segment.append(new_turtle)

    def reset(self):
        for seg12 in self.segment:
            seg12.goto(1000, 1000)
        self.segment.clear()
        self.Create_snake()
        self.head = self.segment[0]

    def extend(self):
        self.add_seg(self.segment[-1].position())

    def Move(self):
        for seg_number in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_number - 1].xcor()
            new_y = self.segment[seg_number - 1].ycor()
            self.segment[seg_number].goto(new_x, new_y)
        self.segment[0].forward(MOVE_BY)

    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)
