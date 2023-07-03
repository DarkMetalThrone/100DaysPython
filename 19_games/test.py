from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

# listen makes the screen stay up and listen for keyboard inputs
screen.listen()

#onkey => this binds a key press to a fucntion
# this makes it a higher order function!!
screen.onkey(key = "space", fun = move_forward)
screen.exitonclick()
