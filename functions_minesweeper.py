def initialise_board():
    '''
    This function initialises the grid to the minesweeper
    game. This only display the 1-D list array, with '0'

    Input: No inputs

    Outputs: list representing the minesweeper board (containign

    '''
    return ['O' for i in range(25)]
board = initialise_board()

def display_board(board):
    '''
    This function displays the 5x5 board. Where X characters are hidden
    as O, which represents the square that has not been selected

    Input: board = a list representing the board

    Output : no output
    '''
    new_board = board.copy()
    for i in range(len(board)):
        if board[i] == 'X':
            new_board[i] = 'O'

    for i in range(0, len(board),5):
        print(new_board[i:i+5])
    return

def insert_mines(board, positions):
    '''
    This function inserts mines to the board at specific positions, the mines
    should be represented by the X character

    Input:
        board = a list representing the board
        positions = a list of lists representing each mine location

    Output: updated board
    '''
    for pos in positions:
        row = pos[0]
        column = pos[1]
        board[row * 5 + column] = 'X'
    return board


def count_adjacent_mines(board, row, column):

    '''
    This function counts the number of mines, X, adjacent (not diagonal) to the selcted position

    Input:
         board = a list representing the board
         row = an int representing the row (0-4) of the square being checked for adjacent mines
         column = : an int representing the column (0-4) of the square being checked for adjacent mines.

    Output: an int representing the number of adjacent mines
    '''
    adjacent_mines = 0

    # above
    if (row-1) >= 0 and board[(row-1)*5 + column] == 'X':
        adjacent_mines += 1
    # below
    if (row+1) < 5 and board[(row+1)*5 + column] == 'X':
        adjacent_mines += 1
    # right
    if (column+1) >= 0 and board[(column+1)*5 + row] == 'X':
        adjacent_mines += 1
    # left
    if (column-1) < 5 and board[(column-1)*5 + row] == 'X':
        adjacent_mines += 1
    return adjacent_mines


def play_turn(board, row, column):

    '''
    This function plays a turn using the provided row and column on the provided board.
    If a hidden mine is selected, it should be changed to a # character, else it should
    add a '_' character if mine was not selected.

    Inputs:
         board = a list representing the board
         row = an int representing the row (0-4) of the square being checked for adjacent mines
         column = : an int representing the column (0-4) of the square being checked for adjacent mines.

    Outputs:
    1. Updated board represented by a list
    2. bool with a value True was selected and False otherwise

    '''
    if board[row * 5 + column] == "X":
        board[row * 5 + column] = "#"
        return board, True
    else:
        adjacent = count_adjacent_mines(board, row, column)
        if adjacent == "O":
            board[row * 5 + column] = " "
        else:
            board[row * 5 + column] = str(adjacent)
        return board, False


def check_win(board):
    '''
    This function determines if the player has won the game, which returns as True.
    This only occurs when all positions that do not contain a mine have been selected.

    Input:
         board = list representing the board

    Output:
    a bool representing if the game has been won (True) or has not been won (False).
    '''
    for position in board:
        if position != "O" and position != "#":
            return False
    return True

def play_game(position):
    '''
    This function runs the game from start to finish

    Input: positions = a list of lists indicating the positions that mines will be placed in the board.

    Output: no outputs
    '''
    board = initialise_board()
    insert_mines(board, position)
    display_board(board)

    while True:
        user_input = input("Enter row and column (separated by space): ").split()
        row, column = map(int, user_input)

        # Implement turn logic here based on user's input
        # For simplicity, let's assume revealing a cell by updating the board directly
        if board[row * 5 + column] == -1:
            print("Game over! You hit a mine.")
            break
        else:
            # Implement the logic for revealing cells or flagging mines
            # For simplicity, let's just reveal the cell
            print("You revealed a safe cell.")
            board[row*5 + column] = 0
            display_board(board)

            # Check if the game is won
            if check_win(board):
                print("Congratulations! You've won the game!")
                break
