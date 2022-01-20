# -*- coding: utf-8 -*- #

"""Импортируем games.even и logic."""
from brain_games.games import even
from brain_games.logic import games_logic


def main():
    """Скрипт запускающий игру brain-even."""
    games_logic(even)


if __name__ == '__main__':
    main()
