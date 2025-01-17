
from Deck import Deck
import time

'''
 Create 2 decks
 Shuffle the decks
 draw one card and compare
 append both cards to the winner, pop from loser 
 incase of ==, pop 6 cards from each player, winner takes all. 
 game ends when one of the players has no cards in the deck or pas the round limit 
'''

value_1 = 0
value_2 = 0
round_counter = 0 #do not change 

lowest_deck_length = 10 # When one of the player has X cards in the deck he will lose
max_rounds = 1000 # If there are no winnders after X rounds the game will end 

# Get the actual value of the card in an integer
def get_card_value(deck):
    return (deck.all_cards[0].get_value())

# Print the card that was drawn
def print_card(deck):
    return deck.all_cards[0]

# Check if either deck is empty and if so will finish the game,
# will also finish the game if its plassed maximum rounds
def game_end(deck_1, deck_2, counter):
    if counter > max_rounds:
        print("Game too long") #checks if we past the round limit and determines the winner based on more cards
        if len(deck_1.all_cards) > len(deck_2.all_cards):
            print("Player one wins with more cards!")
            return True
        else:
            print("Player two wins with more cards!")
            return True
    if len(deck_2.all_cards) < lowest_deck_length:
        print("Game finished - player one won!")
        return True
    elif len(deck_1.all_cards) < lowest_deck_length:
        print("Game finished - player two won!")
        return True
    else:
        return False

# func will run in case of draw of the same value from both players 
def war(deck_1, deck_2, again=0):
    print("\nWAR!!")
    # make a list for 6 cards of each player - winner takes all
    try:
        war_list = [deck_1.all_cards[0], deck_1.all_cards[1], deck_1.all_cards[2], deck_1.all_cards[3], deck_1.all_cards[4], deck_1.all_cards[5],
                    deck_2.all_cards[0], deck_2.all_cards[1], deck_2.all_cards[2], deck_2.all_cards[3], deck_2.all_cards[4], deck_2.all_cards[5]]
        print(f"Player one fights with {deck_1.all_cards[5+again]}")
        print(f"Player two fights with {deck_2.all_cards[5+again]}")
    except:
        if len(deck_1.all_cards) > len(deck_2.all_cards):
            exit("Player one won - couldn't fight")
        else:
            exit("Player two won - couldn't fight")
    # If the first player wins
    if deck_1.all_cards[5+again].get_value() > deck_2.all_cards[5+again].get_value():
        print("Player one won the war")
        win(deck_1, war_list) # add the war_list we made
        deck_1.remove_6_cards() # Removes top 6 cards 
        deck_2.remove_6_cards() #
    elif deck_2.all_cards[5+again].get_value() > deck_1.all_cards[5+again].get_value():
        print("Player two won the war")
        win(deck_2, war_list)
        deck_1.remove_6_cards() # Removes top 6 cards 
        deck_2.remove_6_cards() #
    else:
        again +=1 # in case there is another tie we will draw the next card
        war(deck_1, deck_2, again) # rerun war() with the next card
        
def win(deck, win_card_list):
    deck.add_cards(win_card_list)


def main(round_counter):
    # Creating a decks
    deck_1 = Deck()
    deck_2 = Deck()

    # shuffeling the decks
    deck_1.shuffle_deck()
    deck_2.shuffle_deck()
    while not game_end(deck_1, deck_2, round_counter):

        print("\nRound", round_counter)
        
        # Draw card and get Value (Value is the integer of the card so we can compare them)
        print(f"Player one drew - {print_card(deck_1)}")
        print(f"Player two drew - {print_card(deck_2)}")
        value_1 = get_card_value(deck_1)
        value_2 = get_card_value(deck_2)
        
        if value_1 == value_2:
            war(deck_1, deck_2)

        if value_1 > value_2:
            win(deck_1, [deck_1.all_cards[0], deck_2.all_cards[0]])

        if value_2 > value_1:
            win(deck_2, [deck_1.all_cards[0], deck_2.all_cards[0]])

    
        print("Player one deck has:",  len(deck_1.all_cards), "cards")
        print("Player two deck has:", len(deck_2.all_cards), "cards")

        deck_1.remove_card()
        deck_2.remove_card()
        round_counter +=1
        # time.sleep(0.05)
    else:
        exit("FINISHED")


if __name__ == "__main__":
    try:
        main(round_counter)

    except KeyboardInterrupt:
        exit()
