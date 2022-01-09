# -*- coding: utf-8 -*- #

"""Импортируем games.even и .logic"""
from brain_games.games.even import brain_even
from brain_games.logic import games_logic


def main():
    idgame = 1
    games_logic(brain_even, idgame)


if __name__ == '__main__':
    main()
