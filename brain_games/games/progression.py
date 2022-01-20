# -*- coding: utf-8 -*- #

"""Импортируем random."""
from random import SystemRandom

# Константы.
RULE = 'What number is missing in the progression?'
LEN_PROGRESSION = (5, 11)
LEN_STEP = (1, 10)


def get_round_data():
    """Функция игры brain-progression.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    progression = get_progression()
    correct_answer = get_random_element(progression)
    progression[progression.index(correct_answer)] = '..'
    question_data = ' '.join(progression)
    question = '{0}'.format(question_data)
    return correct_answer, question


def get_progression():
    """Функция генерации прогресии.

    Returns:
        progression: арифметическая прогрессия.
    """
    cryptogen = SystemRandom()
    rand_lenght = cryptogen.randrange(*LEN_PROGRESSION)
    rand_step = cryptogen.randrange(*LEN_STEP)
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
