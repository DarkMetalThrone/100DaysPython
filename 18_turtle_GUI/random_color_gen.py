import turtle as T
import random

# directions
directions = [0, 90, 180, 270]

t = T.Turtle()
#change the line width
t.width(15)
#change the speed
t.speed("fastest")
# change the color mode
T.colormode(255)

def random_color():
    """Returns a tuple containing random values for RGB"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range (200):
    # use setheading instead of right or left just so that it makes sense
    t.setheading(random.choice(directions))
    t.color(random_color())
    t.forward(25)

#open the screen and exit on click
screen = T.Screen()
screen.exitonclick()