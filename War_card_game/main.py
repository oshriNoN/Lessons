
from War_card_game.Class import Deck


'''
 Create a deck for each player 
 Shuffle the deck
 draw one card and compare
 append both cards to the winner, pop from loser 
 incase of ==, pop 3 cards from each player, winner takes all. 
 game ends when one of the players has no cards in the dekc
'''

#Creating a deck for each player 
deck_1 = Deck()
deck_2 = Deck()

#shuffeling the deck
deck_1.shuffle_deck()
deck_2.shuffle_deck()

# print(deck_1.get_ranks())


