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
    
# Letting the Player Choose X or O
def inputPlayerLetter():
    # Let the player enter which letter they want to be.
    # Returns a list with the player's letter as the first item and the computer's letter as the second.
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    # The first element in the list is the player's letter; the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

# Deciding Who Goes First
def whoGoesFirst():
    # Randomly choose which player goes first.
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
    
# Placing a Mark on the Board.
def makeMove(board, letter, move):
    board[move] = letter

# Checking Whether the Player Won.
def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.
    return((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
           (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
           (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
           (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
           (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
           (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
           (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
           (bo[9] == le and bo[5] == le and bo[1] == le) ) # Diagonal

# Duplicating the Board Data
def getBoardCopy(board):
    # Make a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

# Checking Whether a Space on the Board is Free
def isSpaceFree(board, move):
    # Return True if the passed move is free on the passed board.
    return board[move] == ' '

# Letting the Player Enter a Move
def getPlayerMove(board):
    # Let the player enter their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

# Choosing a Move from a List of Moves
def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# Creating the Computer's AI
def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

# Checking Whether the Computer Can Win in One Move
    # Here is the algorithm for Tic-Tac-Toe AI:
    # First, check if we can win in the next move.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
# Checking Whether the Player Can Win in One Move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
# Checking the Corner, Center, and Side Spaces
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return None
    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
