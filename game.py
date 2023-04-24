from enum import Enum, auto
import pyfiglet
from match import Match
from player import Player, HumanPlayer
from square_board import SquareBoard
from list_utils import reverse_matrix
from beautifultable import BeautifulTable
from settings import *


class RoundType (Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()


class DifficultyLevel (Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Game:
    def __init__(self, round_type=RoundType.COMPUTER_VS_COMPUTER, match=Match(Player("chip"), Player("chop"))):
        # Guardar valores recibidos
        self.round_type = round_type
        self.match = match
        # tablero vacio sobre el q jugar
        self.board = SquareBoard()

    def start(self):
        # Imprimo el nombre o logo del juego
        self.print_logo()
        # configuro la partida
        self.configure_by_user()
        # arranco el game loop
        self._start_game_loop()

    def print_logo(self):
        logo = pyfiglet.Figlet(font="starwars")
        print(logo.renderText("Conecta"))

    def _start_game_loop(self):
        # bucle infinito

        while True:
            # obtengo el jugador de turno
            current_player = self.match.next_player
            # le hago jugar
            current_player.play(self.board)
            # muestro su jugada
            self.display_move(current_player)
            # imprimo el tablero
            self.display_board()
            # si el juego ha terminado ...
            if self._is_game_over():
                # muestro el resultado final
                self.display_result()
                # salgo del bucle
                break

    def configure_by_user(self):
        # Le pido al usuario los valores que él quiere para cada tipo de partida y nivel de dificultad
        # determinar el tipo de partida (preguntando al usuario)
        self.round_type = self._get_round_type()
        # crear la partida
        self.match = self.make_match()

    def _get_round_type(self):
        # le pido al usuario que elija el typo de partida
        raw = None
        print("type of Match:\n"
              "1) Computer vs Computer\n"
              "2) Computer vs Human\n")
        while raw != "1" and raw != "2":
            raw = input("Please Select 1 or 2: ")
            if raw == "1":
                return RoundType.COMPUTER_VS_COMPUTER
            else:
                return RoundType.COMPUTER_VS_HUMAN

    def make_match(self):

        if (self.round_type == RoundType.COMPUTER_VS_COMPUTER):
            player1 = Player("Wall-e")
            player2 = Player("EVA")

        else:
            player1 = Player("Bender")
            player2 = HumanPlayer(input("say your name, Human: "))
        return Match(player1, player2)

    def display_move(self, current_player):
        print(f'\n {current_player.namePlayer} has played with ({current_player.player}) in column {current_player.lastMove}')

    def display_board(self):
        matrix = self.board.as_matrix()
        matrix = reverse_matrix(matrix)
        bt = BeautifulTable()
        for column in matrix:
            bt.columns.append(column)

        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]

        # bt.column_headers
        print(bt)

    def display_result(self):
        winner = self.match.get_winner(self.board)
        if winner != None:
            print(f'\n{winner.namePlayer} ({winner.player}) Wins!!')
        else:
            print(
                f'\n A tie between {self.match.get_player("x").namePlayer} (x) and  {self.match.get_player("o").namePlayer} (o)')

    def _is_game_over(self):
        winner = self.match.get_winner(self.board)
        if winner != None:
            # hay un vencedor
            return True
        elif self.board.is_full():
            # un empate
            return True
        else:
            return False
