import random
from Card import Card, suits, ranks

class Deck:    
    def __init__(self):
        self.all_cards = []
        for suit in suits:            
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def get_all_cards(self):
        return self.all_cards
    
    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def remove_card(self):
        return self.all_cards.pop(5)

    def get_all_cards_len(self):
        return len(self.all_cards)
    
    def add_cards(self, new_cards):
        # Adds a new card if its 1 card
        # Adds several Card to a list in case of a war
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        pass
            
    
deck = Deck()
x : Card = deck.all_cards[7].get_value()
print(x)
# print(x.get_value())


