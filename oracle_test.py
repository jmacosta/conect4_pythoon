from square_board import *
from oracle import *
from player import Player


def test_base_oracle():
    board = SquareBoard.fromList([[None, None, None, None],
                                 ['x', 'o', 'x', 'o'],
                                 ['o', 'o', 'x', 'x'],
                                 ['o', None, None, None]])
    expected = [ColumnRecomendation(0, ColumnClassification.MAYBE),
                ColumnRecomendation(1, ColumnClassification.FULL),
                ColumnRecomendation(2, ColumnClassification.FULL),
                ColumnRecomendation(3, ColumnClassification.MAYBE),
                ]
    rappel = BaseOracle()

    assert len(rappel.get_recommendation(board, None)) == len(expected)
    assert rappel.get_recommendation(board, None) == expected


def test_equality():
    cr = ColumnRecomendation(2, ColumnClassification.MAYBE)

    assert cr == cr  # son identicos
    assert cr == ColumnRecomendation(
        2, ColumnClassification.MAYBE)  # equivalente

    # No son equivalentes (no tiene misma clasificación)

    assert cr != ColumnRecomendation(2, ColumnClassification.FULL)
    assert cr != ColumnRecomendation(3, ColumnClassification.FULL)


def test_hash():
    cr = ColumnRecomendation(2, ColumnClassification.MAYBE)

    assert cr.__hash__ == cr.__hash__  # son identicos


def test_is_winning_move():
    winner = Player('Xavier', 'x')
    loser = Player('Otto', 'o')

    empty = SquareBoard()
    almost = SquareBoard.fromList([['o', 'x', 'o', None],
                                   ['o', 'x', 'o', None],
                                   ['x', None, None, None],
                                   [None, None, None, None]])
    oracle = SmartOracle()
    # sobre tablero vacio
    for i in range(0, BOARD_LENGTH):
        assert oracle._is_wining_move(empty, i, winner) == False
        assert oracle._is_wining_move(empty, i, loser) == False
    # sobre tablero almost
        for i in range(0, BOARD_LENGTH):
            assert oracle._is_wining_move(almost, i, loser) == False
    assert oracle._is_wining_move(almost, 2, winner) == True


"""
def test_is_lossing_move():
    me = Player('Xavier', 'x')
    rival = Player('Otto', 'o', opponent=me)

    almost = SquareBoard.fromList([['o', 'x', 'o', None],
                                   ['x', 'o', 'o', None],
                                   ['x', None, None, None],
                                   [None, None, None, None]])
    oracle = SmartOracle()

    # sobre tablero almost
    assert oracle._is_losing_move(almost, 2, me) == True
    assert oracle._is_losing_move(almost, 3, rival) == False
"""


def test_no_good_options():
    x = Player('Xavier', 'x')
    o = Player('Otto', 'o', opponent=x)
    print(x.opponent)
    oracle = SmartOracle()

    maybe = SquareBoard.fromBoardRawCode('....|o...|....|....')
    band_and_full = SquareBoard.fromBoardRawCode('x...|oo..|o...|xoxo')
    all_bad = SquareBoard.fromBoardRawCode('x...|oo..|o...|....')

    assert oracle.no_good_options(maybe, x) == False
    assert oracle.no_good_options(band_and_full, x)
    assert oracle.no_good_options(all_bad, x)
