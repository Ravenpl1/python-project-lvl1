# -*- coding: utf-8 -*- #

"""Импорт brain_calc."""
from brain_games.scripts import brain_calc


def test_brain_calc():
    """Функция игры brain-calc."""
    assert brain_calc.__name__ == 'brain_games.scripts.brain_calc'
