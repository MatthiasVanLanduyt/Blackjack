def game ():

    from classes.player import Player     

    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.\n\n')

    #Create Player
    name = input ("What is your player's name?")
    chips = int(input('How much money do you want to play with?'))
    player = Player(name, chips)    
    
    #Loop Game
    
    continue_game = True
    
    while continue_game == True:  
        print(f'\n{player.name} has {player.chips.total} dinero!')
        player.place_bet()
        
        round (player)
        
        continue_input = input('\n Do you want to play again? Y or N')
        if continue_input[0] in ('y', 'Y'):
            continue_input = True
        else: 
            continue_input = False

def round (player):
    
    from classes.deck import Deck
    from classes.card import Card
    from classes.hand import Hand

    #Initiate new deck and hands
    deck = Deck()
    deck.shuffleCards()
    playerhand = Hand()
    dealerhand = Hand()
    
    #InitialRound
    dealerhand.add_card(deck.dealOneCard())
    dealerhand.add_card(deck.dealOneCard())
    
    playerhand.add_card(deck.dealOneCard())
    playerhand.add_card(deck.dealOneCard())

    playerhand.show_all(player.name)
    dealerhand.show_some('Dealer')


    #Player plays

    playing = play_on (playerhand)
    
    while playing:
        playerhand.add_card(deck.dealOneCard())
        playerhand.show_all(player.name)
        
        if playerhand.value > 21:
            
            player_busts(player)
            break
        
        playing = play_on (playerhand)

    #Dealer plays
    if playerhand.value <= 21:      
                
        dealerhand.show_all('Dealer')
    
        while dealerhand.value < playerhand.value:
            print('\nDealer draws')
            dealerhand.add_card (deck.dealOneCard())
            dealerhand.show_all('Dealer')
            print (f'Dealer has {dealerhand.value}.')

        
        if dealerhand.value <= 21:
            dealer_wins(player)
        else:
            dealer_busts(player)

def play_on(hand):

    print (f'\nYou have {hand.value}.')
    
    
    while True:
        action = input ('Stay or Hit?')
        action = action.capitalize()
        if action in ('Stay', 'Hit'):
            if action == 'Stay':
                return False
            else:
                return True
        else:
            print('Not a valid response')


def player_busts(player):
    print("Player busts!")
    player.chips.lose_bet()

def player_wins(player):
    print("Player wins!")
    player.chips.win_bet()

def dealer_busts(player):
    print("Dealer busts!")
    player.chips.win_bet()
    
def dealer_wins(player):
    print("Dealer wins!")
    player.chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


game()