from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        """has all the base attributes and calls the plank create function"""
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white", "red")
        self.penup()
        self.goto(x= x, y= y)
        self.shapesize(5, 1)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)