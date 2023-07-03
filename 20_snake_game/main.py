from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import time

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
#turn off the tracer for better animation
screen.tracer(0)

#create the snake object, food object and the score baord object
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

#lisen for keypresses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#get the snake to move
game_is_on = True
while game_is_on:
    #make sure the animation is clean so change the frequency of screen refresh
    screen.update()
    time.sleep(0.1)
    #call the move function to set things in motion
    snake.move()

    #detect collision with food
    # distance is a method in turtle which returns the distance between objects
    if snake.head.distance(food) < 15:
        food.refresh_food_pos()
        snake.extend()
        scoreboard.track_score()

    #detect collision with Edges
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with tail
    # trigger game over sequence
    """
    for cell in snake.celllist:
        #beacuse the head is the first cell in the loop and always close to the head
        if cell == snake.head:
            pass
        elif cell.distance(snake.head) < 10:
            game_is_on = False
            scoreboard.game_over()
    """
    for cell in snake.celllist[1:]:
        if cell.distance(snake.head) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()