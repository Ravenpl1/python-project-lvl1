# -*- coding: utf-8 -*- #

"""Импортируем games.calc и .logic"""
from brain_games.games.gcd import brain_gcd
from brain_games.logic import games_logic


def main():
    idgame = 3
    games_logic(brain_gcd, idgame)


if __name__ == '__main__':
    main()