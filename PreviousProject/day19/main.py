from turtle import Turtle, Screen
import random
# day 19 project 2
is_race_on=False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="bet ", prompt="enter the turtle color :")
print(user_bet)
color_list = ["red", "blue", "green", "orange", "black","gray"]
y_pos = [150, 100, 50, 0, -50 ,-100]
turtle_list=[]
for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(color_list[turtle_index])
    tim.up()
    tim.goto(-230, y_pos[turtle_index])
    turtle_list.append(tim)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() >230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print("you win")
            else:
                print("lost")
        rand_distance=random.randint(1,10)
        turtle.forward(rand_distance)
screen.exitonclick()

# day 19 drawing project 1 draw with w ,a,s,d key
# screen.listen()
#
#
# def down():
#     tim.backward(10)
#
#
# def up():
#     tim.forward(10)
#
#
# def left():
#     tim.left(90)
#
#
# def right():
#     tim.right(90)
#
# def clear1():
#     tim.clear()
# screen.onkey(fun=down, key="s")
# screen.onkey(fun=up, key="w")
# screen.onkey(fun=left, key="a")
# screen.onkey(fun=right, key="d")
# screen.onkey(fun=clear1, key="c")
#
# screen.exitonclick()
