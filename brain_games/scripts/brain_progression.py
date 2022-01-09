# -*- coding: utf-8 -*- #

"""Импортируем games.progression и .logic"""
from brain_games.games.progression import brain_progression
from brain_games.logic import games_logic


def main():
    idgame = 4
    games_logic(brain_progression, idgame)


if __name__ == '__main__':
    main()
