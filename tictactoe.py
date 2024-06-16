# Tic_Tac_Toe
import random
# Printing the Board on the Screen
def drawBoard(board):
    # This function prints out the board that it was passed.
    # "Board" is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])