#Display Art
import art
import random
import game_data

score = 0
game_end = False
print(art.logo)

##use if statement to check if user is correct
def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_dscr = account["description"]
    account_country = account["country"]
    return(f"{account_name},a {account_dscr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    """compares followers and returns if the choice is true or false"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
#making the correct guess as account A for the next guess
account_b = random.choice(game_data.data)

#make the game repeateable
while not game_end:
    #Generate a random account from the given data
    account_a = account_b
    account_b = random.choice(game_data.data)
    while account_a == account_b:
        account_b = random.choice(game_data.data)

    #Format account data inot printable format
    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}")
    #Ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #check if the user is right
    ##Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #print the logo here
    print(art.logo)
    
    #Give user feedback on their games
    #score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_end = True

    #clear the screen between rounds