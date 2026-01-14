class Hand: 
    def __init__(self):

        ## Cards in hand

        self.cards = []

    ## Adding a card to hand 

    def addCard(self,card):
        self.cards.append(card)

    ## Total value of the cards
    
    def value(self):
        total = 0
        for card in self.cards:
            total += card.value
        return total

