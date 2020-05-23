# main blackjack application

__author__ = "Jon Ryan"
__version__ = "0.0.1"

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
        self._player1 = ""
        self._player2 = ""
        self._playercards = []
        self._dealercards = []
        self._card1 = 0
        self._card2 = 0
        self._dealercard1 = 0
        self._dealercard2 = 0
        self._inhandvalue = 0

    def dealhand(self, player1=None, player2=None):
        while len(self._playercards) != 2:
            self._playercards.append(random.choice(CARDS))
            self._card1 = self._playercards[-1][0]
            self._card2 = self._playercards[0][0]
            if len(self._playercards) == 2:
                print("You have", self._card1, "&", self._card2)
        while len(self._dealercards) != 2:
            self._dealercards.append(random.choice(CARDS))
            self._dealercard1 = self._dealercards[-1][0]
            self._dealercard2 = self._dealercards[0][0]
            if len(self._dealercards) == 2:
                # [-1] gets the last element in the iterable
                print("Dealer has X &", self._dealercards[-1][0])
        return
    
    def checkhand(self, player=None, dealer=None):
        self._card1 = self._playercards[-1][1]
        self._card2 = self._playercards[0][1]
        playerhand = sum([self._card1, self._card2])
        # checking player cards
        if playerhand > 21:
            if self._card1 or self._card2 == 11:
                self._inhandvalue = playerhand - 10
                print("You have a total of", self._inhandvalue, ", hit or stay?")
                # option = input("You have a total of", self._inhandvalue, ", hit or stay?")
            else:
                print("You busted!")
        elif playerhand == 21:
            print("Blackjack!")
        else:
            self._inhandvalue = playerhand
            print("You have a total of", self._inhandvalue, ", hit or stay?")
        
    def hit(self):
        pass

    def stay(self):
        pass




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
        if option.lower() is 'hit':
            game.hit()
        elif option.lower() is 'stay':
            game.stay()
        else:
            print("Invalid option.")
            game.checkhand()
        
        break


if __name__ == "__main__":
    main()