from settings import *
from linear_board import *
from list_utils import collapse_matrix
from string_utils import explode_list_of_strings


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

    @classmethod
    def fromBoardCode(cls, board_code):
        return cls.fromBoardRawCode(board_code.raw_code)

    @classmethod
    def fromBoardRawCode(cls, board_raw_code):
        """ 
        Recibo un tablero codificado y devuelve un nuevo tablero con su información descodificada
        """
        matrix = []
        matrix = board_raw_code.split('|')
        # decodifico la string en una matriz
        matrix = explode_list_of_strings(matrix)
        # reemplazo los caracterres no validos en la matrz
        matrix = replace_all_in_matrix(matrix, '.', None)
        # creo un tablero en con la matriz
        return cls.fromList(matrix)

    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)]

    def __eq__(self, other):
        # Si son clases distintas son distintos
        if not isinstance(other, self.__class__):
            return False
        else:
            return (self._columns) == (other._columns)
        # si son de la misma clase comparo propiedades de uno y otro

    def __hash__(self):
        return hash(self._columns)

    def __len__(self):
        return len(self._columns)

    def __str__(self) -> str:
        return "tablero vacio"

    def __repr__(self) -> str:
        return self.__str__()

    def is_full(self):
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result

    def add(self, index, token):
        self._columns[index].add(token)

    def as_matrix(self):
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
        m = self.as_matrix()
        d = displace_matrix(m)
        tmp = SquareBoard.fromList(d)
        return tmp.any_horizontal_victory(player)

    def any_sinking_victory(self, player):
        m = self.as_matrix()
        d = displace_matrix(reverse_matrix(m))
        tmp = SquareBoard.fromList(d)
        return tmp.any_horizontal_victory(player)

    def is_victory(self, player):
        return self.any_vertical_victory(player) or self.any_horizontal_victory(player) or self.any_rising_victory(player) or self.any_sinking_victory(player)

    def as_code(self):
        """ 
        Codifico el tablero actual y lo devuelvo como un nuevo objeto de tableros codificados
        """
        return BoardCode(self)


# dunders
def __repr__(self):
    return f'{self.__class__}: {self._columns}'


class BoardCode():
    def __init__(self, board) -> None:
        self._raw_code = collapse_matrix(board.as_matrix())

    @property
    def raw_code(self):
        return self._raw_code

    def __repr__(self) -> str:
        return f'{self.__class__}: {self._raw_code}'

    def __eq__(self, other) -> bool:
        # Si son clases distintas son distintos
        if not isinstance(other, self.__class__):
            return False
        else:
            return (self._raw_code) == (other._raw_code)
        # si son de la misma clase comparo propiedades de uno y otro

    def __hash__(self) -> int:
        return hash(self._raw_code)
