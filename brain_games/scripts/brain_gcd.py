# -*- coding: utf-8 -*- #

"""Импортируем games.gcd и logic."""
from brain_games.games.gcd import brain_gcd
from brain_games.logic import games_logic

# Константы.
RULE = 'Find the greatest common divisor of given numbers.'


def main():
    """Скрипт запускающий игру brain-gcd."""
    games_logic(brain_gcd, RULE)


if __name__ == '__main__':
    main()
