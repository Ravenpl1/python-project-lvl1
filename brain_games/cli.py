# -*- coding: utf-8 -*- #

"""Импортируем prompt."""
import prompt


def welcome_user():
    """Функция приветствует и возвращает введенное имя.

    Returns:
        user: return user name.
    """
    user = prompt.string('Welcome to the Brain Games! \nMay I have your name? ')
    print('Hello, {0}!'.format(user))
    return user
