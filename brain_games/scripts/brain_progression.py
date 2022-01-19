# -*- coding: utf-8 -*- #

"""Импортируем games.progression и logic."""
from brain_games.games.progression import brain_progression
from brain_games.logic import games_logic

# Константы.
RULE = 'What number is missing in the progression?'


def main():
    """Скрипт запускающий игру brain-progression."""
    games_logic(brain_progression, RULE)


if __name__ == '__main__':
    main()
