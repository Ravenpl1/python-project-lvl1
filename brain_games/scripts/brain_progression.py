# -*- coding: utf-8 -*- #

"""Импортируем games.progression и logic."""
from brain_games.games import progression
from brain_games.logic import games_logic


def main():
    """Скрипт запускающий игру brain-progression."""
    games_logic(progression)


if __name__ == '__main__':
    main()
