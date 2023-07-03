from turtle import Turtle, Screen
import random

# directions and colours
directions = [0, 90, 180, 270]
colours = ["navy", "dark slate gray", "dark orange", "medium violet red", "blue violet", "gold", "chartreuse"]

t = Turtle()
#change the line width
t.width(15)
#change the speed
t.speed("fastest")

for _ in range (200):
    # use setheading instead of right or left just so that it makes sense
    t.setheading(random.choice(directions))
    t.color(random.choice(colours))
    t.forward(25)

#open the screen and exit on click
screen = Screen()
screen.exitonclick()