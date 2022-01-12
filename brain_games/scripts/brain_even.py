# -*- coding: utf-8 -*- #

"""Импортируем games.even и .logic"""
from brain_games.games.even import brain_even
from brain_games.logic import games_logic


def main():
    games_logic(brain_even)


if __name__ == '__main__':
    main()
