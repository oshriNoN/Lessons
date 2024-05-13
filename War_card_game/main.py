
from Deck import Deck
import time

'''
 Create 2 decks
 Shuffle the decks
 draw one card and compare
 append both cards to the winner, pop from loser 
 incase of ==, pop 3 cards from each player, winner takes all. 
 game ends when one of the players has no cards in the dekc
'''
value_1 = 0
value_2 = 0
round_counter = 0

# Get the actual value if the card
def get_card_value(deck):
    return (deck.all_cards[0].get_value())

## Print the card the was drawn
def print_card(deck):
    return deck.all_cards[0]

## Check if either deck is empty and if so will finish the game
def game_end(deck_1, deck_2, counter):
    if counter >= 100:
        print("Game too long")
        return True
    if len(deck_2.all_cards) == 0:
        print("Game finished - player one won!")
        return True
    elif len(deck_1.all_cards) == 0:
        print("Game finished - player two won!")
        return True
    else:
        return False

def war(deck_1, deck_2, again=0):
    print("WAR!!")
    #make a list for 5 cards of each player - winner takes all
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
        again +=1
        war(deck_1, deck_2, again)
        
def win(deck, win_card_list):
    deck.add_cards(win_card_list)

# #Creating a decks
deck_1 = Deck()
deck_2 = Deck()

# shuffeling the decks
deck_1.shuffle_deck()
deck_2.shuffle_deck()

while not game_end(deck_1, deck_2, round_counter):

    # Draw card and get Value
    print(f"\nPlayer one drew - {print_card(deck_1)}")
    print(f"Player two drew - {print_card(deck_2)}")

    value_1 = get_card_value(deck_1)
    value_2 = get_card_value(deck_2)
    
    if value_1 == value_2:
        war(deck_1, deck_2)

    if value_1 > value_2:
          win(deck_1, [deck_1.all_cards[0], deck_2.all_cards[0]])

    if value_2 > value_1:
          win(deck_2, [deck_1.all_cards[0], deck_2.all_cards[0]])

  
    print(len(deck_1.all_cards))
    print(len(deck_2.all_cards))

    deck_1.remove_card()
    deck_2.remove_card()
    round_counter +=1
    print(round_counter)
    time.sleep(0.05)
else:
    exit("FINISHED")