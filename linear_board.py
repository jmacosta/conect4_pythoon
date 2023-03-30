from settings import *


class LinearBoard():
    def __init__(self):
        self._column = [None for i in range(BOARD_LENGTH)]

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
        line = 0
        for i in range(BOARD_LENGTH):
            if (self._column[i] == player):
                line += 1
            elif (line < VICTORY_STRIKE):
                line = 0
        return (line == VICTORY_STRIKE)
