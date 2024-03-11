def initialise_board():
    """
    *This function initialises the minesweeper grid before the game starts*
    Arguments
    ---------
    none

    Returns
    -------
    board - A list that represents the minesweeper board that contains 25 'O's in a single row.


    Notes
    -------
    (postcondition 1) Must return an array of 25 'O's in a single row, like this ['O',...,'O']
    """
    return ['O' for i in range(25)] # Return 25 item list as the output
    
def display_board(board):
        """
    *This function displays the board on the output screen as a 5x5 board*
    Arguments
    ---------
        board - a list representing the board of 25 items, which are 'O's

    Returns
    -------
        none

    Notes
    -------
        (precondition 1) Must initialise an array of 25 'O's in a single row, like this ['O',...,'O']
        (postcondition 1) Must print out the 5X5 board like this, ['O','O','O','O','O'], but multiply this row 5 times
    """
    updated_board = board.copy()
    # This for loop replaces the already inserted 'X's and hides it as a 'O'
    for i in range(len(board)):
        if board[i] == 'X':
            updated_board[i] = 'O'
    # This for loop prints out the list and divides it into 5 rows
    for i in range(0, len(board), 5):
        print(updated_board[i:i + 5])
    return

def insert_mines(board, positions):
    """
    *This function inserts mines (in the form of 'X') in certain positions on the board*
    Arguments
    ---------
        board - a list representing the board of 25 items, which are 'O's
        positions - a list of lists representing each mine location. The first

    Returns
    -------
        board - updated board
    Notes
    -------
        (precondition 1) Must initialise an array of 25 'O's in a single row, like this ['O',...,'O']
        (postcondition 1) Must print out updated board like this, (1st row) ['O','O','X','O','O'], if row = 0, and
        column = 2.
    """
    # Iterate through each position to mark on the board
    for pos in positions:
    # Extract row and column from the current position
        row = pos[0]
        column = pos[1]
    # Inserts the extracted row and column positions with 'X'
        board[row * 5 + column] = 'X'
    return board

def count_adjacent_mines(board, row, column):
"""
    *This function counts the number of mines to the selected row, column position (this includes diagonals)*
    Arguments
    ---------
        board- a list representing the board
        r - an int representing the row (0-4) of the square being checked for adjacent mines.
        c - an int representing the column (0-4) of the square being checked for adjacent mines.
    Returns
    -------
        adjacent_mines - an integer that represent the number of adjacent mines on the specified position
    Notes
    -------
        (precondition 1) Make sure edge are implemented, for e.g. if the left corner had any mines next to it, it cannot
        [ 1, 'X']
        ['0', '0']
        (postcondition 1) The adjacent number outputed must be an integer not a string
        like this
        [ 1, 'X']
        ['0', '0']
    """
    adjacent_mines = 0

    # Check upper-left position (diagonal)
    if row > 0 and column > 0 and board[(row - 1) * 5 + column - 1] == 'X':
        adjacent_mines += 1

    # Check upper position
    if row > 0 and board[(row - 1) * 5 + column] == 'X':
        adjacent_mines += 1

    # Check upper-right position (diagonal)
    if row > 0 and column < 4 and board[(row - 1) * 5 + column + 1] == 'X':
        adjacent_mines += 1

    # Check left position
    if column > 0 and board[row * 5 + column - 1] == 'X':
        adjacent_mines += 1

    # Check right position
    if column < 4 and board[row * 5 + column + 1] == 'X':
        adjacent_mines += 1

    # Check lower-left position (diagonal)
    if row < 4 and column > 0 and board[(row + 1) * 5 + column - 1] == 'X':
        adjacent_mines += 1

    # Check lower position
    if row < 4 and board[(row + 1) * 5 + column] == 'X':
        adjacent_mines += 1

    # Check lower-right position (diagonal)
    if row < 4 and column < 4 and board[(row + 1) * 5 + column + 1] == 'X':
        adjacent_mines += 1

    return adjacent_mines

def play_turn(board, row, column):
"""
    *This function is used to play a turn using the provided row and column on the provided board.*
    Arguments
    ---------
        board - a list representing the board
        r - an int representing the row (0-4) of the square being checked for adjacent mines.
        c - an int representing the column (0-4) of the square being checked for adjacent mines.
    Returns
    -------
        board - a list representing the updated board
        bool - a bool with a value True if mine was selected and False otherwise

    Notes
    -------
         (precondition 1) if mine was selected the character of X must change
         (precondition 2) if mine was not selected the character of O must change
         (postcondition 1) if mine was selected the character of X must change to '#'
         (postcondition 2) if mine was not selected the character of O must change to ' '
    """
    # This block ensures that the position entered is within the 0 to 4 range
    if not (0 <= row < 5 and 0 <= column < 5):
        print("Position out of range") # This will output if the position numbers are beyond the 0 to 4 range
        return board, False

    index = row * 5 + column
    if board[index] == "X":
        board[index] = "#"  # Indication that mine has been selected
        return board, True

    adjacent = count_adjacent_mines(board, row, column)
    if adjacent == 0:
        board[index] = " "  # Set to whitespace if no adjacent mines
    else:
        board[index] = str(adjacent)

    return board, False

def check_win(board):
    """
    *This function determines whether the player has won the game or not*
    Arguments
    ---------
        board - a list representing the board

    Returns
    -------
        bool - a bool value where if the game has been won (True) or has not been won (False)
    Notes
    -------
        (precondition 1) if the function returns False, it means the game has not been won yet.
        (postcondition 1) To ensure this, make sure that the all non-mine positions have been selected
    """
    for position in board:
        # If any cell is not a mine and is still hidden ('O'), return False
        if position != "O" and position != "#":
            return False
    # If all non-mine positions have been selected, without 'X' being selected,       
    return True

def play_game(position):
    """
    *This function allows the game to run from start to finish*
    Arguments
    ---------
        positions - a list of lists that indicate the positions that mines will be placed on the board
    Returns
    -------
        none
    Notes
    -------
       (precondition 1) use the split function to separate the 'listed' rows and columns are 's[lit' properly
       (preconditon 2) Always request input while user has not won or lost yet.
    """
    board = initialise_board()
    insert_mines(board, positions) # Mines are inserted in respective places

    print("Initial board:")
    display_board(board)

    while True:
        user = input("Enter row and column (make sure to separate the numbers by a space, (e.g. '4 3')): ")
        row, column = map(int, user.split()) # split function is used to separate the known rows and columns

        updated_board, mine_selected = play_turn(board, row, column) # Player's turn

        print("Updated board:")
        display_board(updated_board) # Displays updated board everytime a turn happens

        if mine_selected:
            print("Game over! Mine Hit")
            break
        elif check_win(updated_board):
            print("Congratulations! You WIN!!!")
            break
