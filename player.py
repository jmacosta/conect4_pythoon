from oracle import BaseOracle, ColumnClassification, ColumnRecomendation


class Player():
    def __init__(self, namePlayer, player, oracle=BaseOracle()):
        self.namePlayer = namePlayer
        self.player = player
        self._oracle = oracle

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
        self._play_on(board, best.index)

    def _ask_oracle(self, board):
        # Obtenemos las recomendaciones
        recommendations = self._oracle.get_recommendation(board, self)
        # seleccionamos la mejor
        best = self._choose(recommendations)
        return (best, recommendations)

    def _play_on(self, board, numColumn):
        board.add(numColumn, self.player)
        pass

    def _choose(self, recommendations):
        valid = list(
            filter(lambda x: x.classification !=
                   ColumnClassification.FULL, recommendations))
        return valid[0]


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


class HumanPlayer(Player):

    def __init__(self, namePlayer, player):
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
