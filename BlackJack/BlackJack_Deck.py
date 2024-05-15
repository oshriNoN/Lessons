import random
from BlackJack_Card import Card, suits, ranks

class Deck:    
    def __init__(self):
        self.all_cards = []
        for suit in suits:            
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def remove_card(self):
        self.all_cards.pop(0)

    def draw_top(self):
        return self.all_cards[0]


    def __str__(self):
        pass
