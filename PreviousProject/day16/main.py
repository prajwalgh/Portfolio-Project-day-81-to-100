# from turtle import *
#
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.pencolor("red")
#
# my_screen = Screen()
# for i in range(0,500,100):
#         timmy.right(i)
#         timmy.forward(i)
#
#
# my_screen.exitonclick()
from prettytable import PrettyTable

# create object
table = PrettyTable()
# accessing  methods
table.add_column('name', ["a", "b", "c"])
table.add_column('age', [1, 3, 4])
# accessing attributes
table.align = "r"
print(table)
