# -*- coding: utf-8 -*- #

"""Импортируем random."""
from random import SystemRandom

# Константы.
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
LEN_RANDOM = (0, 100)


def brain_even():
    """Функция игры brain-even.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    rand_num1 = SystemRandom().randrange(*LEN_RANDOM)
    correct_answer = 'yes' if rand_num1 % 2 == 0 else 'no'
    question = 'Question: {0}'.format(rand_num1)
    return {
        'correct_answer': correct_answer,
        'rule': RULE,
        'question': question,
    }
