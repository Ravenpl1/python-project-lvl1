# -*- coding: utf-8 -*- #

"""Импортируем games.calc и logic."""
from brain_games.games.calc import brain_calc
from brain_games.logic import games_logic


def main():
    """Скрипт запускающий игру brain-calc."""
    games_logic(brain_calc)


if __name__ == '__main__':
    main()
