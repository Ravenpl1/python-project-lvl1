# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
from brain_games.cli import welcome_user


def main():
    """Главный вызов.

    Returns  # noqa: DAR201
    """
    user = welcome_user()
    print('Hello, {0}!'.format(user))
    return user


if __name__ == '__main__':
    main()
