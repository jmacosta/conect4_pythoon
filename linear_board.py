from settings import *


class LinearBoard():
    board = []

    def __init__(self):
        pass

    def __str__(self) -> str:
        return "tablero vacio"

    def __repr__(self) -> str:
        return self.__str__()

    def is_full(self):
        if (len(self.board) < BOARD_LENGTH):
            return False
        else:
            return True

    def add(self, token):
        self.board.append(token)

    def is_tie(self, playerA, playerB):
        pass

    def is_victory(self, player):
        return False
