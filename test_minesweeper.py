import pytest
from functions_minesweeper import *
def test_insert_mines():
    board = [
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O'
    ]
    positions = [ [2, 3], [1, 4] ]
    updated_board = insert_mines(board, positions)
    assert(updated_board == [
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'X',
        'O', 'O', 'O', 'X', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O'
    ])

def test_count_adjacent_mines_in_corner():
    board = [
        'O', 'O', 'O', 'O', 'X',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O'
    ]
    counts = count_adjacent_mines(board, 0, 3)
    assert (counts == 1)

def test_play_turn():
    board = [
        'X', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
    ]
    updated_board, mine_selected = play_turn(board, 1, 1)

    assert updated_board != "Game Over"
    assert isinstance(mine_selected, bool)
def test_check_win_when_all_mines_selected():
    board = [
        'X', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O',
    ]
    assert not check_win(board)

