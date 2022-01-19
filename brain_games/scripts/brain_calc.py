# -*- coding: utf-8 -*- #

"""Импортируем games.calc и logic."""
from brain_games.games.calc import brain_calc
from brain_games.logic import games_logic

# Константы.
RULE = 'What is the result of the expression?'


def main():
    """Скрипт запускающий игру brain-calc."""
    games_logic(brain_calc, RULE)


if __name__ == '__main__':
    main()
