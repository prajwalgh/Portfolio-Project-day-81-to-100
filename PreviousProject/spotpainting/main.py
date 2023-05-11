# import colorgram
import random
import turtle as tur
from turtle import Turtle,Screen
# colors = colorgram.extract('hirst-1.jpg', 60)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb = (r, g, b)
#     rgb_color.append(new_rgb)
# print(rgb_color)
color_list = [(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38),
              (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16),
              (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45),
              (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8),
              (181, 186, 213), (46, 72, 57), (168, 201, 212), (100, 137, 144)]


tur.colormode(255)
t=Turtle()
t.speed("fastest")
t.hideturtle()
t.up()
t.goto(-350,-300)
def draw(x):
    for _ in range(14):
        t.dot(20, random.choice(color_list))
        t.forward(50)


    rotate(x)
def rotate(x):
    if x%2==0:
        t.dot(20, random.choice(color_list))
        t.left(90)
        t.forward(60)
        t.left(90)
    else:
        t.dot(20, random.choice(color_list))
        t.right(90)
        t.forward(60)
        t.right(90)

for i in range(11):
    draw(i)




screen=Screen()
screen.exitonclick()