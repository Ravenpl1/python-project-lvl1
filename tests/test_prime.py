# -*- coding: utf-8 -*- #

"""Импорт brain_prime."""
from brain_games.games import prime


def test_prime():
    """Функция теста игры brain_prime."""
    correct_answer, question = prime.get_round_data()
    assert type(correct_answer) is str
    assert type(question) is str
