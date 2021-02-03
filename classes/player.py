from classes.chips import Chips

class Player:
    def __init__ (self, name, chips = 0):
        self.name = name
        self.chips = Chips(chips)
    
    def __str__(self) -> str:
        return self.name

    def place_bet (self):
        while True:
            try:
                self.chips.bet = int(input('How many chips would you like to bet? '))
            except ValueError:
                print('Sorry, a bet must be an integer!')
            else:
                if self.chips.bet > self.chips.total:
                    print("Sorry, your bet can't exceed",self.chips.total)
                else:
                    break