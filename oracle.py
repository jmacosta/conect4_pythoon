from enum import Enum, auto
from square_board import *
from copy import deepcopy


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
            # Solo se compara la clasificación
            return self.classification == other.classification

    def __hash__(self) -> int:
        return hash(self.classification)


class ColumnClassification(Enum):
    FULL = -1
    MAYBE = 10
    WIN = 100
    BAD = 1


class BaseOracle():
    def __init__(self):
        pass

    def __str__(self):
        return "Oraculo Base"

    def __rpr__(self):
        return self.__str__

    def _get_column_recomendation(self, board, index, player):
        """
        Clasifica como FULL o MAYBE y devuelve una ColumnRecommedation
        """
        columnValue = ColumnClassification.MAYBE
        if board._columns[index].is_full():
            columnValue = ColumnClassification.FULL
        return ColumnRecomendation(index, columnValue)

    def get_recommendation(self, board, player):
        """
        Devuelve una lista de columnRecomendations
        """
        listRecomendation = []
        for index in range(len(board)):
            listRecomendation.append(
                self._get_column_recomendation(board, index, player))
        return listRecomendation


class SmartOracle(BaseOracle):

    def _get_column_recomendation(self, board, index, player):
        """
        indica una posible mejora de MAYBE
        """
        recommendation = super()._get_column_recomendation(board, index, player)
        if recommendation.classification == ColumnClassification.MAYBE:
            # Se puede Mejorar
            if self._is_wining_move(board, index, player):
                recommendation.classification = ColumnClassification.WIN
            elif self._is_losing_move(board, index, player):
                recommendation.classification = ColumnClassification.BAD
        return recommendation

    def _is_wining_move(self, board, index, player):
        """
        determina si al jugar una posicion nos llevaria a ganar de inmediato
        """
        # hago una copia del tablero
        # juego en ella
        tmp = self.play_on_tmp_board(board, index, player)
        # determino si hay una victoria para player o no
        return tmp.is_victory(player.player)

    def play_on_tmp_board(self, board, index, player):
        """
        Crea una copia del board y juega en él 
        """
        tmp = deepcopy(board)
        tmp.add(index, player.player)
        return tmp

    def _is_losing_move(self, board, index, player):
        """
        determina si al jugar una posicion facilito la victoria al oponente
        """
        # hago una copia del tablero
        # juego en ella
        will_lose = False
        tmp = self.play_on_tmp_board(board, index, player)
        # hago una jugada con mi oponente y determino si el ganaria o no
        for i in range(BOARD_LENGTH):
            if self._is_wining_move(tmp, i, player._opponent):
                will_lose = True
                break
        return will_lose

    def no_good_options(self, board, player):
        """ 
        Tengo que jugar en todas las columnas y determinar si todas son malas jugadas
        """
        noOptions = True
        for i in range(BOARD_LENGTH):
            noOptions = self._is_losing_move(board, i, player)
        return noOptions


class MemoizingOracle(SmartOracle):
    """ 
    el metdodo get_recomendation está ahora moemoizado
    """

    def __init__(self):
        super().__init__()
        self._past_recomendations = {}

    def _make_key(self, board_code, player):
        """ 
        la clave debe de combinar el board y el player
        """
        return f'{board_code.raw_code}@{player.player}'

    def get_recommendation(self, board, player):
        # creamos la clave
        key = self._make_key(board.as_code(), player)
        # miramos el cache si no esta calculo y guardo el cache
        if key not in self._past_recomendations:
            self._past_recomendations[key] = super(
            ).get_recommendation(board, player)
        # devuelvo lo que esta en cache
        return self._past_recomendations[key]


class LearningOracle(MemoizingOracle):

    def update_to_bad(self, board_code, player, position):
        # crear clave
        key = self._make_key(board_code, player)
        # obtener la clasificacion erronea
        recommendation = self.get_recommendation(
            SquareBoard.fromBoardCode(board_code), player)
        # corregirla
        recommendation[position] = ColumnRecomendation(
            position, ColumnClassification.BAD)
        # sustituirla
        self._past_recomendations[key] = recommendation
