from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self) -> None:
        """initialize the snake with default attributes, length/ positions"""
        self.step_distance = 20
        self.celllist = []
        self.create_snake()
        self.head = self.celllist[0]

    def create_snake(self):
        for i in START_POSITION:
            # add the first segments
            self.add_segment(i)
            
    # a function to add segments
    def add_segment(self, position):
        cell = Turtle("square")
        cell.penup()
        cell.color("white", "red")
        cell.goto(position)
        self.celllist.append(cell)

    # extend the snake when the score increases
    def extend(self):
        self.add_segment(self.celllist[-1].position())

    #get the snake to move
    def move(self):
        """gets the snake to start moving"""
        for i in range(len(self.celllist)-1, 0, -1):
            #iterate backwards and make the cells follow the cells ahead of them
            new_x = self.celllist[i-1].xcor()
            new_y = self.celllist[i-1].ycor()
            self.celllist[i].goto(new_x, new_y)

        #move the first cell here!
        self.celllist[0].forward(self.step_distance)
    
    #change direction of the snake
    #change the heading of the first cell the rest will follow
    #make sure the sanke cant fold back on itself!!!
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):        
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):        
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
