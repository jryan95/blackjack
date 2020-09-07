# main blackjack application

__author__ = "Jon Ryan"
__version__ = "0.0.2"

import random

CARDS = {
    0 : ("A", 11),
    1 : ("1", 1),
    2 : ("2", 2),
    3 : ("3", 3),
    4 : ("4", 4),
    5 : ("5", 5),
    6 : ("6", 6),
    7 : ("7", 7),
    8 : ("8", 8),
    9 : ("9", 9),
    10 : ("J", 10),
    11 : ("Q", 10),
    12 : ("K", 10)
}

class Blackjack():
    def __init__(self):

        self.cards = {
            'dealer': {
                'cards': [],
                'card1': 0,
                'card2': 0,
                'card3': 0,
                'card4': 0,
                'card5': 0,
                'inhandvalue': 0,
            },
            'player1' : {
                'name': '',
                'cards': [],
                'card1': 0,
                'card2': 0,
                'card3': 0,
                'card4': 0,
                'card5': 0,
                'inhandvalue': 0,
            },
            'player2': {
                'name': '',
                'cards': [],
                'card1': 0,
                'card2': 0,
                'card3': 0,
                'card4': 0,
                'card5': 0,
                'inhandvalue': 0,
            },
        }

    def dealhand(self, player1=None, player2=None):
        while len(self.cards['player1']['cards']) != 2:
            self.cards['player1']['cards'].append(random.choice(CARDS))
            self.cards['player1']['card1'] = self.cards['player1']['cards'][-1][0]
            self.cards['player1']['card2'] = self.cards['player1']['cards'][0][0]
        
        while len(self.cards['dealer']['cards']) != 2:
            self.cards['dealer']['cards'].append(random.choice(CARDS))
            self.cards['dealer']['card1'] = self.cards['dealer']['cards'][-1][0]
            self.cards['dealer']['card2'] = self.cards['dealer']['cards'][0][0]
        
        print(f"You have {self.cards['player1']['card1']} & {self.cards['player1']['card2']}.")
        print(f"Dealer is showing a {self.cards['dealer']['cards'][-1][0]}.")
    
    def _check_cards(player=None, dealer=None):
        """ Check if cards are assigned, otherwise assign them. """
        for

    def checkhand(self, player=None, dealer=1):
        # Assign integer values
        self.cards['player1']['card1'] = self.cards['player1']['cards'][-1][1]
        self.cards['player1']['card2'] = self.cards['player1']['cards'][0][1]
        playerhand = sum([self.cards['player1']['card1'], self.cards['player1']['card2']])

        dealerhand = sum([self.cards['player1']['card1'], self.cards['player1']['card2']])
        self.cards['dealer']['card1'] = self.cards['dealer']['cards'][-1][1]
        self.cards['dealer']['card2'] = self.cards['dealer']['cards'][0][1]

        # checking dealer cards
        if dealerhand > 21:
            if self.cards['dealer']['card1'] or self.cards['dealer']['card2'] == 11:
                self.cards['dealer']['inhandvalue'] = dealerhand - 10
            else:
                print("Dealer busts, you win!")
        elif dealerhand == 21:
            print("Dealer wins!")
        elif dealerhand < 18:
            self.hit(dealer)
        else:
            self.cards['dealer']['inhandvalue'] = dealerhand
        
        # checking player cards
        if playerhand > 21:
            if self.cards['player1']['card1'] or self.cards['player1']['card2'] == 11:
                self.cards['player1']['inhandvalue'] = playerhand - 10
                print(f"You have a total of {self.cards['player1']['inhandvalue']}, hit or stay?")
                # option = input("You have a total of", self._inhandvalue, ", hit or stay?")
            else:
                print("You busted!")
        elif playerhand == 21:
            print("Blackjack!")
        else:
            self.cards['player1']['inhandvalue'] = playerhand
            print(f"You have a total of {self.cards['player1']['inhandvalue']}, hit or stay?")


    def hit(self, dealer=0):
        if dealer != 0:
            self.cards['dealer']['cards'].append(random.choice(CARDS))
            print(f"The dealer now has {self.cards['dealer']['cards']}.")
        else:
            self.cards['player1']['cards'].append(random.choice(CARDS))
            print(f"You now have {self.cards['player1']['cards']}.")

    def stay(self):
        cardstotal = self.cards['player1']['cards'][0][1] + self.cards['player1']['cards'][1][1]
        print(f"You have stayed at {cardstotal}.")
        

def main():
    print('Welcome to Blackjack v{} by {}'.format
    (__version__, __author__))
    print("**" * 20)
    
    # Used for checking if it is first game or not, if not, previous winner goes first
    # first_game = True
    game = Blackjack()
    # Main game loop
    while True:
        print("Dealing hand...")
        game.dealhand()
        print("**" * 20)
        game.checkhand()
        option = input(">> ")
        if option.lower() == 'hit' or option.lower() == 'h':
            game.hit()
        elif option.lower() == 'stay' or option.lower() == 's':
            game.stay()
        else:
            print("Invalid option.")
            game.checkhand()
        
        break


if __name__ == "__main__":
    main()