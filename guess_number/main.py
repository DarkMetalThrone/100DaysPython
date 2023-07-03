#print the logo
import art
import random

print(art.logo)
print("Welcome to the NUMBER GUESSING game.")
#global constant is the random number chosen from the range 0 to 100
NUMBER = random.randint(0, 101)

#set the game to run until it is stopped
end_of_game = False

#let the player chose the difficulty
difficulty = input("Chose the difficulty - 'easy' or 'hard': ")

#set the lives based on the choice of difficulty
if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
#invalid input means the game ends immediately, and the while loop never gets executed
else:
    print("Invalid Input")
    end_of_game = True


#keep the user guessing until he wins or looses all his lives
while not end_of_game and lives > 0:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess < NUMBER:
        lives -= 1
        print("You went too LOW")
        print(f"You have {lives} lives left.")
    elif guess > NUMBER:
        lives -= 1
        print("You went too HIGH")
        print(f"You have {lives} lives left.")
    else:
        print("Yay! you guessed correct!!")
        end_of_game = True

#if the player runs out of lives
if lives == 0:
    print("Looks like you ran out of lives, YOU LOSE!")