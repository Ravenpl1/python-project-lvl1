# -*- coding: utf-8 -*- #

"""Импортируем random."""
from random import SystemRandom

# Константы.
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LEN_RANDOM = (0, 100)


def get_round_data():
    """Функция игры brain-prime.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    rand_num1 = SystemRandom().randrange(*LEN_RANDOM)
    num_is_prime = is_prime(rand_num1)
    correct_answer = 'yes' if num_is_prime else 'no'
    question = '{0}'.format(rand_num1)
    return correct_answer, question


def is_prime(number):
    """Функция предикат простого числа.

    Args:
        number: число.

    Returns:
        bool: True если число простое.
    """
    if number < 2:
        return False
    for element in range(2, int(number / 2) + 1):
        if number % element == 0:
            return False
    return True
