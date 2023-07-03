# make the turtle draw a painting 
# painting dimension = 10 dots X 10 dots => 650 X 650
# dot size = 20
# dot spacing = 50

import turtle as T
import random
from data import colour_list

#create turlte object and initial settings
t = T.Turtle()
t.penup()
t.hideturtle()
#set color mode to 255
T.colormode(255)
t.speed(0)


t.setpos(-250, -250)

# method 1
# for _ in range(10):
#     for count in range (10):
#         #dot takes two parameters, size and color
#         t.dot(20, random.choice(colour_list))
#         t.forward(50)
#     t.left(90)
#     t.forward(50)
#     t.left(90)
#     t.forward(500)
#     t.right(180)

#method 2
for dot_count in range (1, 101):
    # dot takes two parameters, size and color
    t.dot(20, random.choice(colour_list))
    t.forward(50)
    # if the dots are a multiple of 10
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

#make the screen stay open
screen = T.Screen()
screen.screensize(300, 300)
print(screen.screensize())
screen.exitonclick()