# This program recretes the game edge and sketch
#you can control the turtle with WSAD keys
#press SPACE to reset the screen
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def clock_wise():
    tim.right(5)

def anti_clock():
    tim.left(5)

def clear():
    # tim.clear() #erases all the drawings made by this turtle
    # tim.penup() #so that the turtle dosent draw the line returning to the centre
    # tim.home() #returns the turtle to the centre
    # tim.pendown() #it can draw again
    tim.reset()

screen.listen()

screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "d", fun = clock_wise)
screen.onkey(key = "a", fun = anti_clock)
screen.onkey(key = "space", fun = clear)

screen.exitonclick()