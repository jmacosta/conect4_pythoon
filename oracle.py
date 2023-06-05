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
    BAD = 5
    LOSE = 1


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

    def no_good_options(self, board, player):
        """ 
        comprobamos q todas sean de tipo correcto
        """
        columnRecommendations = self.get_recommendation(board, player)
        result = True
        for rec in columnRecommendations:
            if (rec.classification == ColumnClassification.WIN) or (rec.classification == ColumnClassification.MAYBE):
                result = False
                break
        return result
    # metodos a ser sobrescritos por las subclases

    def backtrack(self, listMoves):
        pass

    def update_to_bad(self, move):
        pass


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
                recommendation.classification = ColumnClassification.LOSE
        return recommendation

    def _is_wining_move(self, board, index, player):
        """
        determina si al jugar una posicion nos llevaria a ganar de inmediato
        """
        # hago una copia del tablero
        # juego en ella
        tmp = self.play_on_tmp_board(board, index, player)
        # determino si hay una victoria para player o no
        return tmp.is_victory(player.char)

    def play_on_tmp_board(self, board, index, player):
        """
        Crea una copia del board y juega en él 
        """
        tmp = deepcopy(board)
        tmp.add(index, player.char)
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
        return f'{board_code}@{player.char}'

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

    def update_to_bad(self, move):
        # crear clave
        key = self._make_key(move.boardcode, move.player)
        # obtener la clasificacion erronea
        recommendation = self.get_recommendation(
            SquareBoard.fromBoardCode(move.boardcode), move.player)
        # corregirla
        recommendation[move.position] = ColumnRecomendation(
            move.position, ColumnClassification.BAD)
        # sustituirla
        self._past_recomendations[key] = recommendation

    def backtrack(self, listMoves):
        """
        Repasa todas las jugadas y si encuentra una en la que esta todo perdido tiene que ser acutalizada a BAD
        """
        print('Learning...')
        # los moves estan en orden inverso empiezan por el ultimo
        # por cada move
        for move in listMoves:
            # lo reclasifico a BAD
            self.update_to_bad(move)
            # evaluo si todo estaba perdido tras las clasificacion
            board = SquareBoard.fromBoardCode(move.boardcode)
            if not self.no_good_options(board, move.player):
                # si lo estaba sigo el bucle si no, paro
                break
        print(f'Size of Knowledgebase: {len(self._past_recomendations)}')
