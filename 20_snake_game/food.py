from turtle import Turtle
import random

class Food(Turtle):
    def __init__ (self):
        super().__init__()
        #now the food object has all the turtle attributes and methods
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_food_pos()

    def refresh_food_pos(self):
        #make sure the food doesn't span at the endge of the screen
        self.goto(random.randint(-250, 250), random.randint(-250, 250))