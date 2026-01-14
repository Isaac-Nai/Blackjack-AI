class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value 
        self.hidden = True 

    ## Changes the card's visibility

    def flip(self):
        self.hidden = not(self.hidden)