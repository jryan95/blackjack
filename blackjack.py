# main blackjack application

__author__ = "Jon Ryan"
__version__ = "0.0.1"

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
    
    def prevwinner(self):
        pass

    def dealhand(self, player1, player2):
        pass

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
    else:
        player1 = input("Player 1, please input your name: ")
        print("Prepare to play against the computer.")
        print("**" * 20)
    
    
    first_game = True
    game = Blackjack()
    # Main game loop
    while True:
        if first_game:
        
        game.dealhand(int(player1), int(player2))
        print("Dealing hand...")
        print("**" * 20)




if __name__ == "__main__":
    main()