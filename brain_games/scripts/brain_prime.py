# -*- coding: utf-8 -*- #

"""Импортируем games.prime и .logic"""
from brain_games.games.prime import brain_prime
from brain_games.logic import games_logic


def main():
    idgame = 5
    games_logic(brain_prime, idgame)


if __name__ == '__main__':
    main()
