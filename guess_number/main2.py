#chose a random number betwenn 1 and 100
import random
import art

#set the difficulty lives in a global variable
EASY_LVL_ATTEMPTS = 10
HARD_LVL_ATTEMPTS = 5


#make a funciton to check if the guess is correct
def check_answer(guess, NUMBER, turns):
    """Checks answer against the ANSWER, and returns the number of attempts left"""
    if guess > NUMBER:
        print("  Too HIGH.")
        return turns - 1
    elif guess < NUMBER:
        print("  Too LOW.")
        return turns - 1
    else:
        print(f"You got it! The Number was {NUMBER}")


#function to set the difficulty
def set_difficulty():
    """Sets the number of attempts based on users choices"""
    difficulty = input("Choose a Difficulty, Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        lives = EASY_LVL_ATTEMPTS
    elif difficulty == 'hard':
        lives = HARD_LVL_ATTEMPTS
    return lives


#function that has the game
def game():
    #Game Start Text
    print(art.logo)
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    NUMBER = random.randint(1, 100)
    turns = set_difficulty()

    #set the initial value to be something not in the range
    guess = 0
    while guess != NUMBER and turns > 0:
        #display the numbe rof attempts left
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess
        guess = int(input("Make a Guess: "))
        #check the guess against the actual number and the attempts left
        turns = check_answer(guess, NUMBER, turns)
        #Track the number of attempts left
        if turns == 0:
            print("You have run out of lives, YOU lOSE!!")
            return
        elif guess != NUMBER:
            print("  Guess again.")


game()
