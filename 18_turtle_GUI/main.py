from turtle import Turtle, Screen
import random

timmy = Turtle()
#change the shape
timmy.shape("turtle")
timmy.color("black", "red")

colours = ['black', 'red', 'blue', 'yellow', 'green', 'pink', 'orange', 'purple']

for i in range (3, 11):
    timmy.color(random.choice(colours))
    for j in range (i):
        timmy.forward(100)
        timmy.right(360/ i)




#open the screen at the end and exit on click
screen = Screen()
screen.exitonclick()