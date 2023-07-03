from turtle import Turtle, Screen
import random

screen = Screen()
#since the screen size is crucial to the race make it a fixed dimension
screen.setup(height=400, width=500)
# ask the user to make a bet
user_bet = screen.textinput(title="Make your bet", prompt="Choose the color of the turtle which might win")
race_is_on = False

#color scheme for the turtles
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

#make a list that has turtle objects
turtles = []
#since you have the dimensions of the screen, move the turtles to the left edge
for i in range(len(colours)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x = -230 , y = -100 + i*35)
    turtles.append(new_turtle)

if user_bet:
    race_is_on = True
    #do this do avoid starting the while loop prematurely while the user is still deciding on the bet

while race_is_on:
    for i in turtles:
        if i.xcor() > 230:
            race_is_on = False
            winnning_color = i.pencolor()
            if winnning_color == user_bet:
                print(f"You've Won! The {winnning_color} turtle won the race!! ")
            else:
                print(f"You Lost! The winner was the {winnning_color} turtle.")
        random_distance = random.randint(0,10)
        i.forward(random_distance)

screen.exitonclick()