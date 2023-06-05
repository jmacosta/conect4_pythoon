import pytest
from square_board import *

from settings import BOARD_LENGTH, VICTORY_STRIKE


def test_empty_board():
    empty = SquareBoard()
    assert empty != None
    assert empty.is_full() == False
    assert empty.is_victory('x') == False
    assert empty.is_victory('o') == False


def test_vertical_victory():
    vertical = SquareBoard.fromList([['o', 'x', 'x', 'x'],
                                    [None, None, None, None],
                                    [None, None, None, None],
                                    [None, None, None, None],])
    assert vertical.is_victory('x')
    assert vertical.is_victory('o') == False


def test_horizontal_victory():
    horizontal_victory = SquareBoard.fromList([['x', None, None, None],
                                               ['x', None, None, None],
                                               ['x', 'o', None, None],
                                               ['o', 'o', None, None],
                                               ])
    assert horizontal_victory.is_victory('x')
    assert horizontal_victory.is_victory('o') == False


def test_sinking_victory():
    sinking_victory = SquareBoard.fromList([['x', 'o', 'x', 'o',],
                                           ['x', 'x', 'o', None,],
                                           ['o', 'o', None, None,],
                                           ['o', 'x', None, None,],
                                            ])
    assert sinking_victory.is_victory('o')
    assert sinking_victory.is_victory('x') == False


def test_rising_victory():
    rising_victory = SquareBoard.fromList([['x', 'o', None, None,],
                                           ['o', 'x', None, None,],
                                           ['x', 'o', 'x', 'o',],
                                           ['x', 'o', None, None,],])
    assert rising_victory.is_victory('x')
    assert rising_victory.is_victory('o') == False


def test_compare_columns():
    board_A = SquareBoard.fromList([])
    board_B = SquareBoard.fromList([])
    board_C = SquareBoard.fromList([['x', 'o', None, None,],
                                    ['o', 'x', None, None,],
                                    ['x', 'o', 'x', 'o',],
                                    ['x', 'o', None, None,],])

    board_D = SquareBoard.fromList([['x', 'o', None, None,],
                                    ['o', 'x', None, None,],
                                    ['x', 'o', 'x', 'o',],
                                    ['x', 'o', None, None,],])
    board_E = SquareBoard.fromList([['x', 'o', None, None,],
                                    ['x', 'x', None, None,],
                                    ['x', 'o', 'x', 'o',],
                                    ['x', 'o', None, None,],])

    board_F = SquareBoard.fromList([['x', 'o', None, None,],
                                    ['o', 'x', None, None,],
                                    ['x', 'o', 'x', 'o',],
                                    ['x', 'o', None, None,],])
    assert board_A == board_B
    assert board_C == board_D
    assert (board_E == board_F) == False


def test_board_code():
    board = SquareBoard.fromList([['x', 'o', None, None],
                                 ['o', 'x', None, None],
                                 ['x', 'o', 'x', 'o'],
                                 ['x', 'x', 'o', None]])
    code = board.as_code()
    clone_board = SquareBoard.fromBoardCode(code)
    assert board == board
    assert clone_board == board
