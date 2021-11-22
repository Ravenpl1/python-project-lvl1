#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
from brain_games.cli import welcome_user


def main():
    """Главный вызов."""
    print("Hello, %s!" % welcome_user())


if __name__ == '__main__':
    main()
