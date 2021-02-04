class Hand:

    def __init__(self) -> None:
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def __str__(self) -> str:
        
        return 'Hand is : ' + self.cards + ' with value ' + self.value

    def add_card (self, card):

        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1
        
        self.value = self.value + card.value

        if self.value > 21 and self.aces > 0:
            self.value = self.value - 10
            self.aces -= 1
    
    def show_all (self, name):
        
        print ('\n' + name + "'s hand is: ")
        for card in self.cards:
            print(card)
    
    def show_some (self, name):
        showcards = []

        print ('\n' + name + "'s hand is: ")
        for card in self.cards:
            if card == self.cards[len(self.cards) - 1]:
                print('Hidden card')
            else:
                print(card)
