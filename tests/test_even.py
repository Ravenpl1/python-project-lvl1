# -*- coding: utf-8 -*- #

"""Импорт brain_even."""
from brain_games.games import even


def test_even():
    """Функция теста игры brain_even."""
    generate_data = tuple(even.brain_even().keys())
    assert generate_data == ('correct_answer', 'rule', 'question')
