from turtle import *
from paddle import Paddle
from ball import Ball

#screen attributes
screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.tracer(0)    #turn off the animations

#create plank and the ball as objects
paddle_r = Paddle(350, 0)
paddle_b = Paddle(-350, 0)
ball = Ball()

# Enetr the game
game_is_on = True
while game_is_on:
    screen.update()
    #listen to the user and map keys to motion
    screen.listen()
    screen.onkey(paddle_r.move_up, "Up" )
    screen.onkey(paddle_r.move_down, "Down" )

    screen.onkey(paddle_b.move_up, "w" )
    screen.onkey(paddle_b.move_down, "s" )

screen.exitonclick()