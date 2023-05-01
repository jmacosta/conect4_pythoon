from oracle import BaseOracle, ColumnClassification, ColumnRecomendation
import random
from list_utils import all_same
from move import Move


class Player():
    def __init__(self, namePlayer, player=None, opponent=None, oracle=BaseOracle()):
        self.namePlayer = namePlayer
        self.player = player
        self._oracle = oracle
        self._opponent = opponent
        self.lastMove = None

    @property
    def opponent(self):
        return self._opponent

    @opponent.setter
    def opponent(self, other):
        if other != None:
            self._opponent = other
            other.opponent = self

    def __eq__(other, self):
        if not isinstance(self, other.__class__):
            return False
        else:
            return (self.namePlayer, self.player) == (other.namePlayer, other.player)

    def __hash__(self):
        return hash()

    def __str__(self):
        return "Player"

    def __rpr__(self):
        return f'{self.__class__}'

    def play(self, board):
        # pregunta al oraculo
        (best, recommendations) = self._ask_oracle(board)
        # juega en la mejor
        self._play_on(board, best.index, recommendations)

    def _ask_oracle(self, board):
        # Obtenemos las recomendaciones
        recommendations = self._oracle.get_recommendation(board, self)
        # seleccionamos la mejor
        best = self._choose(recommendations)
        return (best, recommendations)

    def _play_on(self, board, numColumn, recommendations):
        board.add(numColumn, self.player)
        self.lastMove = Move(numColumn, board.as_code(), recommendations, self)

    def _choose(self, recommendations):
        valid = list(
            filter(lambda x: x.classification !=
                   ColumnClassification.FULL, recommendations))
        # ordenamos por valor de classiciacion
        valid = sorted(
            valid, key=lambda x: x.classification.value, reverse=True)
        # si todas son iguales elegimos una random
        if all_same(valid):
            return random.choice(valid)
        else:
            # si no son iguales elegimos la mejor
            return valid[0]

    def on_lose(self):
        pass

    def on_win(self):
        pass


class HumanPlayer(Player):

    def __init__(self, namePlayer, player=None):
        super().__init__(namePlayer, player)

    def _ask_oracle(self, board):
        """
        Le pido al humano 
        """
        while True:
            # pedimos columna al Humano
            raw = input("Intorduzca número de columna: ")
            # verificamos que la respuesta no es erronea
            if _is_int(raw) and _is_within_column_range(board, int(raw)) and _is_non_full_column(board, int(raw)):
                # si no lo es, jugamos donde ha dicho y salimos del bucle
                pos = int(raw)
                return (ColumnRecomendation(pos, None), None)
                # si lo es pregunto otra vez
            pass


class ReportingPlayer(Player):

    def on_lose(self):
        """ 
        Avisa al oraculo si su recomendacion fue un truño
        """
        boardCode = self.lastMove.boardcode
        position = self.lastMove.position
        self._oracle.update_to_bad(boardCode, self, position)

# funciones de validación de indice de columna


def _is_within_column_range(board, index):
    return index >= 0 and index < len(board)


def _is_non_full_column(board, index):
    return not board._columns[index].is_full()


def _is_int(param):
    try:
        num = int(param)
        return True
    except:
        return False
