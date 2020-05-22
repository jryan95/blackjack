# main blackjack application

__author__ = "Jon Ryan"
__version__ = "0.0.1"

import random

CARDS = {
    0 : "A",
    1 : "1",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    10 : "J",
    11 : "Q",
    12 : "K"
}

class Blackjack():
    def __init__(self):
        self._player1 = ""
        self._player2 = ""
        self._player1cards = []
        self._player2cards = []
        self._dealercards = []
    
    def prevwinner(self):
        pass

    def dealhand(self, player1, player2=None):
        while len(self._player1cards) != 2:
            self._player1cards.append(random.choice(CARDS))
            if len(self._player1cards) == 2:
                print("You have ", self._player1cards)

    def hit(self):
        pass




def main():
    print('Welcome to Blackjack v{} by {}'.format
    (__version__, __author__))
    print("**" * 20)
    players = int(input("How many people are playing?: "))
    if players > 2:
        print("Error, can't handle more than 2 players in version {}".format(__version__))
    elif players == 2:
        player1 = input("Player 1, please input your name: ")
        player2 = input("Player 2, please input your name: ")
        two_player = True
    else:
        player1 = input("Player 1, please input your name: ")
        two_player = False
        print("Prepare to play against the dealer.")
        print("**" * 20)
    
    
    first_game = True
    game = Blackjack()
    # Main game loop
    while True:
        if not first_game:
            previous_winner = game.prevwinner()
        
        print("Dealing hand...")
        print("**" * 20)
        if two_player:
            game.dealhand(player1, player2)
        else:
            game.dealhand(player1)

        break




if __name__ == "__main__":
    main()