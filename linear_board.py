from settings import *
from list_utils import *


class LinearBoard():
    @classmethod
    def fromList(cls, list):
        board = cls()
        if (len(list) == BOARD_LENGTH):
            board._column = list
        if (len(list) < BOARD_LENGTH):
            board._column = list
            board._column = [None for i in range((len(list)), BOARD_LENGTH)]
        return board

    def __init__(self):
        self._column = [None for i in range(BOARD_LENGTH)]

    def __hash__(self):
        return hash(self._column)

    def __eq__(self, other):
        # Si son clases distintas son distintos
        if not isinstance(other, self.__class__):
            return False
        else:
            return (self._column) == (other._column)
        # si son de la misma clase comparo propiedades de uno y otro

    def __str__(self) -> str:
        return "tablero vacio"

    def __repr__(self) -> str:
        return self.__str__()

    def is_full(self):
        try:
            self._column.index(None)
        except:
            return True
        return False

    def add(self, token):
        if (not self.is_full()):
            i = self._column.index(None)
            self._column[i] = token

    def is_tie(self, playerA, playerB):
        return ((self.is_victory(playerA) == False) and (self.is_victory(playerB) == False))

    def is_victory(self, player):
        """
        line = 0
        for i in range(BOARD_LENGTH):
            if (self._column[i] == player):
                line += 1
            elif (line < VICTORY_STRIKE):
                line = 0
        return (line == VICTORY_STRIKE)
        """
        # aplicamos nueva funcion

        return find_streak(self._column, player, VICTORY_STRIKE)
