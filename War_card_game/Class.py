'''
Class to define cards with: 
    # Suit (spades, hearts, etc...)
    # Rank (king, jack, eight, etc...)
    # Value (1 - 14)
'''
import random

suits = ("Spades", "Diamonds", "Hearts", "Clubs")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack",
"Queen", "King", "Ace")

value = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11,
"Queen":12, "King":13, "Ace":14}

all_cards = []

deck_value = []

class Cards:
    def __init__(self, suit, rank):
        self.suit = suit ## spades, hearts....
        self.rank = rank ## string of the num (two, three )
        self.value = value[rank] ## number from the rank 

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return int(self.value)
    
    def __str__(self):
        pass


class Deck:    
    def __init__(self):
        self.all_cards = all_cards
        self.deck_value = deck_value
        for suit in suits:            
            for rank in ranks:
                created_card = Cards(suit, rank)
                self.deck_value.append(created_card.value)
                self.all_cards.append(created_card)

    def get_all_cards(self):
        return (self.all_cards)
    
    def shuffle_deck(self):
        return random.shuffle(self.dec)
    
    def get_value(self):
        return self.deck_value
    
    def get_ranks(self):
        pass
    
    def remove_card(self):
        self.all_cards.pop(0)

    def get_all_cards_len(self):
        return len(self.all_cards)
    
    def add_cards(self,new_cards):
        # Adds a new card if its 1 card
        # Adds several cards to a list in case of a war
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self) -> str:
        return self.all_cards

deck = Deck()
card = Cards("Hearts", "Two")
print(type(card.get_value()))

