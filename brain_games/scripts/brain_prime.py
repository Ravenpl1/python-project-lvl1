# -*- coding: utf-8 -*- #

"""Импортируем games.prime и logic."""
from brain_games.games.prime import brain_prime
from brain_games.logic import games_logic

# Константы.
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    """Скрипт запускающий игру brain-prime."""
    games_logic(brain_prime, RULE)


if __name__ == '__main__':
    main()
