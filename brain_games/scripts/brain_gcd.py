# -*- coding: utf-8 -*- #

"""Импортируем games.gcd и logic."""
from brain_games.games.gcd import brain_gcd
from brain_games.logic import games_logic


def main():
    """Скрипт запускающий игру brain-gcd."""
    games_logic(brain_gcd)


if __name__ == '__main__':
    main()
