# -*- coding: utf-8 -*- #

"""Импорт brain_gcd."""
from brain_games.games import gcd


def test_gcd():
    """Функция теста игры brain_gcd."""
    correct_answer, question = gcd.brain_gcd()
    assert type(correct_answer) is int
    assert type(question) is str
