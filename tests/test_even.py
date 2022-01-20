# -*- coding: utf-8 -*- #

"""Импорт brain_even."""
from brain_games.games import even


def test_even():
    """Функция теста игры brain_even."""
    correct_answer, question = even.get_round_data()
    assert type(correct_answer) is str
    assert type(question) is str
