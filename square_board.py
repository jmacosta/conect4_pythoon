from settings import *
from linear_board import *


class SquareBoard():

    @classmethod
    def fromList(cls, list_of_list):
        """
        Transforma lisat de listas en un list de Lineabords
        """
        board = cls()
        board._columns = list(
            map(lambda element: LinearBoard.fromList(element), list_of_list))
        return board

    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)]

    def __str__(self) -> str:
        return "tablero vacio"

    def __repr__(self) -> str:
        return self.__str__()

    def is_full(self):
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result

    def as_matrix(self):
        """
         matrix = []
         for i in range(len(self._columns)):
             matrix[i] = list(self._columns[i]._column)
         return matrix
         """
        return list(
            map(lambda x: x._column, self._columns)
        )

    def any_vertical_victory(self, player):
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(player)
        return result

    def any_horizontal_victory(self, player):
        transp = transponse(self.as_matrix())
        tmp = SquareBoard.fromList(transp)
        return tmp.any_vertical_victory(player)

    def any_rising_victory(self, player):
        return False

    def any_sinking_victory(self, player):
        return False

    def is_victory(self, player):
        return self.any_vertical_victory(player) or self.any_horizontal_victory(player) or self.any_rising_victory(player) or self.any_sinking_victory(player)

# dunders


def __repr__(self):
    return f'{self.__class__}:{self._columns}'
