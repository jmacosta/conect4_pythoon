from square_board import *
from oracle import *


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

    # No son equivalentes

    assert cr != ColumnRecomendation(1, ColumnClassification.MAYBE)
    assert cr != ColumnRecomendation(2, ColumnClassification.FULL)
    assert cr != ColumnRecomendation(3, ColumnClassification.FULL)


def test_hash():
    cr = ColumnRecomendation(2, ColumnClassification.MAYBE)

    assert cr.__hash__ == cr.__hash__  # son identicos
