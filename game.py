import math
import time
from player import HumPlayer, RandCompPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None


    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def make_a_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_in = square // 3
        row = self.board[row_in*3 : (row_in + 1) * 3]
        if all ([s == letter for s in row]):
            return True

        col_in = square % 3
        column = [self.board[col_in+i*3] for i in range(3)]
        if all ([s == letter for s in column]):
            return True

        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if all ([s == letter for s in diag1]):
                return True

            diag2 =[self.board[i] for i in [2, 4, 6]]
            if all ([s == letter for s in diag2]):
                return True
        return False
    
    def empty_square(self):
        return self.board.count(' ')

    
    def num_empty_square(self):
        return len(self.open_moves())


    def open_moves(self):
        moves = []
        for (i,square) in enumerate(self.board):
            if square == ' ':
                moves.append(i)
        return moves


def play(game, x_player, o_player, print_game=True):
    
    print('Welcome to Tic Tac Toe! Let\'s Play!\n')

    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_square():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_a_move(square, letter):
            if print_game:
                print('\n' + letter + f' makes a move to square {square}\n')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
                
        time.sleep(0.5)


    if print_game:
            print('It\'s a tie!')


def main():
    x_player = HumPlayer('X')
    o_player = RandCompPlayer('O')
    t = TicTacToe()
    
    while True:
        play(t, x_player, o_player, print_game = True)
        
        choice=input("\nWould you like to play again? (y/n): ")
        
        if choice=='y'.lower():
            main()
            break
        
        elif choice=='n'.lower():
            print("\nThanks for Playing!")
            break

main()

    




        
