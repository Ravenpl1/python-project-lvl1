# -*- coding: utf-8 -*- #

"""Импортируем games.gcd и logic."""
from brain_games.games import gcd
from brain_games.logic import games_logic


def main():
    """Скрипт запускающий игру brain-gcd."""
    games_logic(gcd)


if __name__ == '__main__':
    main()
