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
                                    [None, None, ],
                                    [None, None, None, None],
                                    [None, None, None, None],
                                    [None, None, None, None]])
    assert vertical.is_victory('x')
    assert vertical.is_victory('o') == False


def test_horizontal_victory():
    horizontal_victory = SquareBoard.fromList([['x', None, None, None],
                                               ['x', None, None, None],
                                               ['x', 'o', None, None],
                                               ['x', 'o', None, None],
                                               ])
    assert horizontal_victory.is_victory('x')
    assert horizontal_victory.is_victory('o') == False


"""
def test_add():
    b = SquareBoard()
    for i in range(BOARD_LENGTH):
        b.add('x')
    assert b.is_full() == True


def test_victory():
    b = SquareBoard()
    for i in range(VICTORY_STRIKE):
        b.add('x')

    assert b.is_victory('o') == False
    assert b.is_victory('x') == True


def test_tie():
    b = SquareBoard()
    b.add('o')
    b.add('o')
    b.add('x')
    b.add('o')

    assert b.is_tie('x', 'o')


def test_add_to_full():
    full = SquareBoard()
    for i in range(BOARD_LENGTH):
        full.add('x')
    full.add('x')
    assert full.is_full() == True
"""
