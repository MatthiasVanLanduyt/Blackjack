import random
from classes.card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:
    
    
    def __init__ (self):

        self.cards = []
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    
    def shuffleCards (self):
        random.shuffle(self.cards)
    
    def dealOneCard (self):
        return self.cards.pop()

