from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        """Creates a score Board"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scorebaord()

    def update_scorebaord(self):
        """text formattiing the scorebaord"""
        self.write(f"Current Score = {self.score}", move = False, align = "center", font = ('Courier', 16, 'normal'))

    def game_over(self):
        """writes GAME OVER when the game ends"""
        self.goto(0, 0)
        self.write(f"GAME OVER!", move = False, align = "center", font = ('Courier', 18, 'bold'))

    def track_score(self):
        """increases the score when the food collides with the snake head"""
        self.clear()
        self.score += 1
        self.update_scorebaord()


