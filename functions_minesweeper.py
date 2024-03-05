def initialise_board():
    return ['O' for i in range(25)]
board = initialise_board()

def display_board(board):
    new_board = board.copy()
    for i in range(len(board)):
        if board[i] == 'X':
            new_board[i] = 'O'

    for i in range(0, len(board),5):
        print(new_board[i:i+5])
    return

def insert_mines(board, positions):
    for pos in positions:
        row = pos[0]
        column = pos[1]
        board[row * 5 + column] = 'X'
    return board


def count_adjacent_mines(board, row, column):
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
    for position in board:
        if position != "O" and position != "#":
            return False
    return True

def play_game(position):
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
