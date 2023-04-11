from enum import Enum, auto
from square_board import *


class ColumnRecomendation():
    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

    def __str__(self):
        return "Recomendación de columnas"

    def __eq__(self, other):
        # Si son clases distintas son distintos
        if not isinstance(other, self.__class__):
            return False
        else:
            return (self.index, self.classification) == (other.index, other.classification)
        # si son de la misma clase comparo propiedades de uno y otro

    def __hash__(self) -> int:
        return hash((self.index, self.classification))


class ColumnClassification(Enum):
    FULL = auto()
    MAYBE = auto()


class BaseOracle():
    def __init__(self):
        pass

    def __str__(self):
        return "Oraculo Base"

    def __rpr__(self):
        return self.__str__

    def get_column_recomendation(self, lb):
        columnValue = ColumnClassification.MAYBE
        if lb.is_full():
            columnValue = ColumnClassification.FULL
        else:
            columnValue = ColumnClassification.MAYBE
        return columnValue

    def get_recommendation(self, board, player):
        listRecomendation = []
        for index in range(len(board)):
            listRecomendation.append(
                ColumnRecomendation(index, self.get_column_recomendation(board._columns[index])))
        return listRecomendation
