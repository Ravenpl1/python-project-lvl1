# -*- coding: utf-8 -*- #

"""Импортируем random."""
from random import SystemRandom


def brain_even():
    """Функция игры brain-even.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    rand_num1 = SystemRandom().randrange(0, 100, 1)
    correct_answer = 'yes' if rand_num1 % 2 == 0 else 'no'
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = 'Question: {0}'.format(rand_num1)
    return {
        'correct_answer': correct_answer,
        'rule': rule,
        'question': question,
    }
