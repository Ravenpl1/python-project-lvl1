# -*- coding: utf-8 -*- #

"""Импортируем random."""
from random import SystemRandom


def brain_prime():
    """Функция игры brain-prime.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    rand_num1 = SystemRandom().randrange(0, 100)
    num1_gcd = devisors(rand_num1)
    correct_answer = 'yes' if len(num1_gcd) == 2 else 'no'
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = 'Question: {0}'.format(rand_num1)
    return {
        'correct_answer': correct_answer,
        'rule': rule,
        'question': question,
    }


def devisors(number):
    """Функция генерации списка делителей.

    Args:
        number: число.

    Returns:
        list: список делителей.
    """
    gcd = []
    for element in range(1, number + 1):
        if number % element == 0:
            gcd.append(element)
    return gcd
