#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
from brain_games.cli import welcome_user


def main():
    """Главный вызов."""
    user = welcome_user()
    print("Hello, %s!" % user)
    return user

if __name__ == '__main__':
    main()
