# -*- coding: utf-8 -*- #

"""Импорт brain_games."""
from brain_games.games import calc


def test_calc():
    """Функция игры brain-progression."""
    data = calc.brain_calc()
    print(tuple(data.keys()))
    assert tuple(data.keys()) == ('correct_answer', 'rule', 'question')
