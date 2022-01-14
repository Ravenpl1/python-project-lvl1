# -*- coding: utf-8 -*- #

"""Импорт brain_prime."""
from brain_games.games import prime


def test_prime():
    """Функция теста игры brain_prime."""
    generate_data = tuple(prime.brain_prime().keys())
    assert generate_data == ('correct_answer', 'rule', 'question')
