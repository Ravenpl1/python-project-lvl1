# -*- coding: utf-8 -*- #

"""Импорт brain_games."""
from brain_games.scripts import brain_games


def test_brain_games():
    """Функция игры brain-progression."""
    assert brain_games.__name__ == 'brain_games.scripts.brain_games'
