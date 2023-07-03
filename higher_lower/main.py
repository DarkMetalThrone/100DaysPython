#Print the LOGO
import art
import game_data
import random

#Global variable keeps track of the score
SCORE = 0

#A function which choses a person different from the ones already chosen
chosen_people = []
def choose_person():
    """Chooses two dissimilar random people and returns the chosen one"""
    #chosing person A
    Z = random.choice(game_data.data)
    return Z

#a function that compares the number of followers
def compare(dict1, dict2):
    """Takes two functions as input and returns the one woth more followers"""
    if dict1['follower_count'] > dict2['follower_count']:
        return dict1
    else:
        return dict2

def game(SCORE):
    """Compare two entities until you choose wrong"""
    end_of_game = False
    A = choose_person()
    #append to a list to make sure not reused
    chosen_people.append(A)
    while not end_of_game:
        #print the game logo for every comparision
        print(art.logo)
        #print entity A
        print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")
        #print the Versus symbol
        print(art.vs)
        #making sure the same person is not chosen
        go = False
        while not go:
            B = choose_person()
            if B in chosen_people:
                continue
            else:
                go = True
        #append the entity B which is definitely different than all the previous entities
        chosen_people.append(B)
        print(f"To B: {B['name']}, {B['description']}, {B['country']}")
        print(f"Your Current Score is: {SCORE}")

        #Ask the player which one has more followers
        choice = input("Who has more followers? A or B: ")
        if choice == "A":
            chosen = A
        elif choice == "B":
            chosen = B
        else:
            print("Invalid Choice! Restart the Program.")
            end_of_game = True

        #If the choice is correct, increase score and make the correct choice entity A
        if compare(A, B) == chosen:
            SCORE += 1
            A = B
        #else the game ends and the score is displayed
        else:
            print(f"You Loose!! Your Score is: {SCORE}")
            end_of_game = True

#play the Damn Game, pass the global variable to keep track of the score
game(SCORE)