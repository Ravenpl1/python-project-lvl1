# -*- coding: utf-8 -*- #

"""Импорт brain_gcd."""
from brain_games.games import gcd


def test_gcd():
    """Функция теста игры brain_gcd."""
    generate_data = tuple(gcd.brain_gcd().keys())
    assert generate_data == ('correct_answer', 'rule', 'question')
