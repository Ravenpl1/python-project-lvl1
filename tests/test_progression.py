# -*- coding: utf-8 -*- #

"""Импорт brain_progression."""
from brain_games.games import progression


def test_progression():
    """Функция теста игры brain_progression."""
    generate_data = tuple(progression.brain_progression().keys())
    assert generate_data == ('correct_answer', 'rule', 'question')
