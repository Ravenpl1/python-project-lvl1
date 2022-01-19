# -*- coding: utf-8 -*- #

"""Импортируем random."""
from random import SystemRandom

# Константы.
LEN_RANDOM = (0, 100)


def brain_even():
    """Функция игры brain-even.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    rand_num1 = SystemRandom().randrange(*LEN_RANDOM)
    correct_answer = 'yes' if rand_num1 % 2 == 0 else 'no'
    question = '{0}'.format(rand_num1)
    return correct_answer, question
