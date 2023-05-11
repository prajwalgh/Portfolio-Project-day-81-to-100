from turtle import Screen
from Paddle import *
from ball import *
import time
from score import *
X=0.1
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)

screen.listen()
paddle_l = Paddle(350, 0)
paddle_r = Paddle(-350, 0)
ball = Ball(0, 0)
score_l = Score(-100, 200)
score_r = Score(100, 200)
screen.onkey(paddle_l.up, "Up")
screen.onkey(paddle_r.upw, "w")
screen.onkey(paddle_l.down, "Down")
screen.onkey(paddle_r.downs, "s")

game_is_on = True
while game_is_on:
    time.sleep(X)
    screen.update()
    ball.move()
    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle_l) < 50 and ball.xcor() > 320 or ball.distance(paddle_r) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_postion()
        # print("left win")
        score_l.score+=1
        if X>0:
            X-=0.001
        score_l.print_score(score_l.score)
    if ball.xcor() < -380:
        ball.reset_postion()
        score_r.score+=1
        if X >0:
             X -= 0.001
        score_r.print_score(score_r.score)
        # print("right win")
screen.exitonclick()
