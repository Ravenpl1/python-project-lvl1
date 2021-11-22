#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем prompt."""
import prompt


def welcome_user():
    """Функция возвращает введенное имя."""
    print('Welcome to the Brain Games')
    return prompt.string('May I have your name? ')
