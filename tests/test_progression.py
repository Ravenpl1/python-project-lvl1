# -*- coding: utf-8 -*- #

"""Импорт brain_progression."""
from brain_games.games import progression


def test_progression():
    """Функция теста игры brain_progression."""
    correct_answer, question = progression.brain_progression()
    assert type(correct_answer) is str
    assert type(question) is str
