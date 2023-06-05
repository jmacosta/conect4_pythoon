import pytest
from player import Player, HumanPlayer
from match import Match

xavier = None
otto = None


def setup():
    global xavier
    xavier = HumanPlayer("Prof. Xavier")
    global otto
    otto = Player("DR. Octopus")


def teardown():
    global xavier
    xavier = None
    global otto
    otto = None


def test_different_players_have_different_chars():
    t = Match(xavier, otto)
    assert xavier.char != otto.char


def test_no_player_witho_none_char():
    t = Match(xavier, otto)
    assert xavier.char != None
    assert otto.char != None


def test_next_player_is_round_robbin():
    t = Match(otto, xavier)
    p1 = t.next_player
    p2 = t.next_player

    assert p1 != p2


def test_players_are_opponents():
    t = Match(otto, xavier)
    x = t.get_player('x')
    o = t.get_player('o')

    assert o.opponent == x
    assert x.opponent == o
