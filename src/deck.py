import random 
from card import Card 

class Deck:
    def __init__(self):
        
        ## Creating the cards and adding them to the deck

        self._cards = []
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        values = [("2",2),("3",3),("4",4),("5",5),("6",6),("7",7),("8",8),
                        ("9",9),("10",10),("J",10),("Queen",10),("King",10),("Ace",1)]
        
        for suit in suits:
            for name , value in values:
                self._cards.append(Card(f"{name} of {suit}", value))
        
    ## Draws a card from the deck

    def draw(self):
        return self._cards.pop()
    
    ## Shuffles the deck

    def shuffle(self):
        random.shuffle(self._cards)
    