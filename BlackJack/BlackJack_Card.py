'''
Class to define cards with: 
    # Suit (spades, hearts, etc...)
    # Rank (king, jack, eight, etc...)
    # Value (1 - 10)
'''

suits = ("Spades", "Diamonds", "Hearts", "Clubs")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack",
"Queen", "King", "Ace")

val_dic = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10,
"Queen":10, "King":10, "Ace":11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit ## spades, hearts....
        self.rank = rank ## string of the num (two, three )
        self.val_dic = val_dic[rank] ## number from the rank 

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.val_dic
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Card):
            raise NotImplemented
        else:
            return self.get_value() == other.get_value()
    
    def __gt__(self, other): ##greather than
        if not isinstance(other, Card):
            raise NotImplemented 
        return self.get_value() > other.get_value()
        
    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self) -> str:
        return self.__str__()
    
    
# card1 = Card("Hearts", "Three")
# card2 = Card("Spades", "Two")

# x = card1.get_value()
# y = card2.get_value()

# print(card1 > card2)
