import random

#Import os to be used to clear console 
import os 

#Define calculate_score function
def calculate_score(cards):
     '''Take a list of cards and return the score for those cards '''
     if sum(cards) == 21 and len(cards) == 2: 
          return 0
     if 11 in cards and sum(cards) > 21:
          cards.remove(11)
          cards.append(1)
     return sum(cards)

def compare(user_score, computer_score):
    '''Compare the scores of both players to determine the winner'''
    if user_score == computer_score:
        return "Draw 🫶"
    elif computer_score == 0:        
        return "Lose, opponent has Blackjack 😭"
    elif user_score == 0:
        return "You win with a Blackjack 😊"
    elif user_score > 21 and computer_score > 21:
        return "Wow you both went over! Bust! Draw 🫶"
    elif user_score > 21:
        return "You went over. Bust!. You lose! 😭"
    elif computer_score > 21:
        return "Opponent went over. Bust! You win! 😊"
    elif user_score > computer_score:
        return "You win! 😊"
    else:
        return "You lose 😭"
    
    

#Define deal card function
def deal_card():
     '''Returns random card from the deck'''
     deck_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
     card = random.choice(deck_of_cards)
     return card

def blackjack():
    '''Plays the game of blackjack'''
    user_cards = []
    #Create empty list for the computers cards
    computers_cards = []
    #Create a list to hold the values of the cards
    



    is_game_over = False
    #For loop to add 2 cards to the user and computers empty card list
    for _ in range(2):
        user_cards.append(deal_card())
        computers_cards.append(deal_card())


    while not is_game_over:
        #Use the calculate score function to record users score
        user_score = calculate_score(user_cards)
        #Use the calculate score function to record computers score
        computer_score = calculate_score(computers_cards)
        #Print users cards and scores
        print(f"Your cards: {user_cards}. Current score: {user_score}")
        #Print the first card in the computers hand
        print(f"Computers first card: {computers_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_card())
        computer_score = calculate_score(computers_cards)
        
    print (compare(user_score, computer_score))
    print (f'Your cards: {user_cards}, Your total: {user_score}')
    print (f'Your opponents cards: {computers_cards}, Your opponents total: {computer_score}')
    
     

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") =="y":
    blackjack()
    ready = input("Press any button: ")
    if ready == "":
        os.system ('cls')
    else:
        os.system ('cls')
