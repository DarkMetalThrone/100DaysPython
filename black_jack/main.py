import art

#random library import
import random

def deal_card():
    """Returns a card from the deck of cards"""
    #deck of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Returns the sum of an iterable"""
    #check for immediate black jack with two cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    #if the sum is greater than 21 and there is an ace in the deck
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """Compares the scores of player and computer to determine the winner"""
    #apparently that's hoe the rules are
    if user_score > 21 and computer_score > 21:
        print("User Loses!")
    
    if user_score == computer_score:
        print("It is a Draw...")
    elif user_score == 0 :
        print("User Wins!!")
    elif computer_score == 0:
        print("Computer Wins!")
    elif user_score > 21:
        print("You went over, You Lose!")
    elif computer_score > 21:
        print("The computer went over, You Win!!")
    elif user_score > computer_score:
        print("You are nearer, You Win!!")
    else:
        print("You Lose!")

def playgame():
    """BlackJack Game as a function"""
    #print the logo
    print(art.logo)
    user_cards = []
    computer_cards = []
    end_of_game = False

    #deal two cards at the start of the game
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not end_of_game:
        #calculate the score for both the decks and print the cards
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Deck: {user_cards} Your Score: {user_score}")
        print(f"Computer's Deck: {computer_cards[0]}")

        #if either player or computer have blackjack or if player exceeds 21 end the game
        if user_score == 21 or computer_score == 21 or user_score > 21:
            end_of_game = True
        #if none of the abpve conditions are true ask the user to deal an extra card or not
        else:
            user_deal_card = input("Do you want another cards? press 'y' or 'n': ")
            if user_deal_card == "y":
                #apparently the card gets added only to the players deck and not the dealers
                user_cards.append(deal_card())
            else:
                end_of_game = True

        #if the computer is not blackjack and score is less than 17 keep dealing the cards
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print(f"    Your Final Deck: {user_cards}   Your Final Score: {user_score}")
    print(f"    Computer's Final Deck: {computer_cards} Computer Score: {computer_score}")
    #make a compare function that will decide the winner at the end
    compare(user_score, computer_score)

while input("Do you want to play a game of BLACKJACK? 'y' or 'n': ") == "y":
    playgame()