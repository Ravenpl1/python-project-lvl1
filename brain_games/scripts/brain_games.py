# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
from brain_games.cli import welcome_user


user = ''

def greeting():
    """Главный вызов.

    Returns  # noqa: DAR201
    """
    global user
    user = welcome_user()
    print('Hello, {0}!'.format(user))


if __name__ == '__main__':
    greeting()
