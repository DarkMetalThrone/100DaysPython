from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.ball.shape("square")
        self.ball.penup()
        self.ball.color("white", "blue")