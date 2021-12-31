import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        spot = random.choice(game.open_moves())
        return spot


class HumPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        valid_spot = False
        val = None
        while not valid_spot:
            spot = input(self.letter + '\'s turn. Input move (0-8): ')

            try:
                val = int(spot)
                if val not in game.open_moves():
                    raise ValueError
                valid_spot = True
            except ValueError:
                print('Invalid spot. Try again.')
                
        return val
