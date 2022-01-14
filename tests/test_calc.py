# -*- coding: utf-8 -*- #

"""Импорт brain_calc."""
from brain_games.games import calc


def test_calc():
    """Функция теста игры brain_calc."""
    generate_data = tuple(calc.brain_calc().keys())
    assert generate_data == ('correct_answer', 'rule', 'question')
