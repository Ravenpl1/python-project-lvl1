# -*- coding: utf-8 -*- #

"""Импорт brain_calc."""
from brain_games.games import calc


def test_calc():
    """Функция теста игры brain_calc."""
    correct_answer, question = calc.brain_calc()
    assert type(correct_answer) is int
    assert type(question) is str
