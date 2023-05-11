import random
import turtle
from random import choice
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(20):
#     tim.down()
#     tim.forward(5)
#     tim.up()
#     tim.forward(5)
# for i in range( 3 , 11):
#     x=360/i
#     y=["red","yellow","green","black","red","yellow","green","black","red","yellow","green","black"]
#     tim.pencolor(y[i])
#     while i!=0:
#         tim.forward(100)
#         tim.right(x)
#         i-=1

# for i in range(1 ,100):
#     for j in range(1,100):
#         tim.goto(i,j)
# tim.width(5)
tim.speed("fastest")
# l = [1, 2, 3]
def random_color():
     r=random.randint(0,255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     randomcolor=(r,g,b)
     return randomcolor
# for _ in range(300):
#     x = choice(l)
#     tim.pencolor(random_color())
#     if x==1:
#         tim.forward(10)
#     elif x==2:
#         tim.right(90)
#         tim.forward(10)
#     elif x==3:
#         tim.left(90)
#         tim.forward(10)
for _ in range(36):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(10)
    tim.circle(100)






screen = Screen()
screen.exitonclick()


