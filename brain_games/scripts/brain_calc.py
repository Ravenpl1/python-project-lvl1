# -*- coding: utf-8 -*- #

"""Импортируем games.calc и .logic"""
from brain_games.games.calc import brain_calc
from brain_games.logic import games_logic


def main():
    """Prints the element given as input

    Args:
        x: any element
    Returns:
        None
    """
    idgame = 2
    games_logic(brain_calc, idgame)


if __name__ == '__main__':
    main()
