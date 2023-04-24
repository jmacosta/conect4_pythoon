class Match():
    def __init__(self, player1, player2):
        player1.player = 'x'
        player2.player = 'o'
        player1.opponent = player2
        self._players = {'x': player1, 'o': player2}
        self._round_robbin = [player1, player2]

    @property
    def next_player(self):
        next = self._round_robbin[0]
        self._round_robbin.reverse()
        return next

    def get_player(self, player):
        return self._players[player]

    def get_winner(self, board):
        # devuelve el ganador y si no devulve None
        if board.is_victory("x"):
            return self.get_player('x')
        elif board.is_victory("o"):
            return self.get_player('o')
        else:
            return None
