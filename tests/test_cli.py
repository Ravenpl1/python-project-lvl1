# -*- coding: utf-8 -*- #

"""Импорт cli."""
from brain_games import cli


def test_cli():
    """Функция интерфейса cli."""
    assert cli.__name__ == 'brain_games.cli'
