# -*- coding: utf-8 -*- #

"""Импортируем random."""
from random import SystemRandom


def brain_progression():
    """Функция игры brain-progression.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    progression = get_progression()
    correct_answer = get_random_element(progression)
    progression[progression.index(correct_answer)] = '..'
    question_data = ' '.join(progression)
    rule = 'What number is missing in the progression?'
    question = 'Question: {0}'.format(question_data)
    return {
        'correct_answer': correct_answer,
        'rule': rule,
        'question': question,
    }


def get_progression():
    """Функция генерации прогресии.

    Returns:
        progression: арифметическая прогрессия.
    """
    cryptogen = SystemRandom()
    max_len = 11
    rand_lenght = cryptogen.randrange(start=5, stop=max_len)
    rand_step = cryptogen.randrange(start=1, stop=10)
    progression = map(
        str, range(rand_step, (rand_lenght * rand_step) + 1, rand_step),
    )
    return list(progression)


def get_random_element(progression):
    """Функция случайного выбора элемента списка.

    Args:
        progression: входящий список.

    Returns:
        progression[rand_item]: элемент списка.
    """
    cryptogen = SystemRandom()
    rand_item = cryptogen.randrange(len(progression))
    return progression[rand_item]
