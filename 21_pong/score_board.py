from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        """Create Score Board"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Text formatting the scoreboard"""
        self.write(self.score, move = False, align = 'left', font = ('courier', 30, 'bold'))

    def game_over(self):
        """Prints GAME OVER on screen"""
        self.goto(0, 0)
        self.write(f"GAME OVER!", move = False, align = "center", font = ('Courier', 36, 'bold'))

    def track_score(self):
        """increases the score when the food collides with the snake head"""
        self.clear()
        self.score += 1
        self.update_scoreboard()
