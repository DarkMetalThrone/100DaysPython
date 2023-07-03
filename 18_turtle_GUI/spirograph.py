import turtle as t
import random


# generate random colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim = t.Turtle()
tim.speed("fastest")
tim.width(4)
t.colormode(255)

# for i in range (0, 360, 10):
#     tim.right(10)
#     tim.color(random_color())
#     tim.circle(100)

def draw_spirograph(offset):
    """draws a spirograph with the passed offset"""
    for _ in range (int(360/ offset)):
        #instead of right() or left() you can use heading and update it with setheading every iteration
        tim.setheading(tim.heading() + offset)
        tim.color(random_color())
        tim.circle(100)

draw_spirograph(10)

#open the screen and exit on click
screen = t.Screen()
screen.exitonclick()