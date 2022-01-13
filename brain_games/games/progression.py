# -*- coding: utf-8 -*- #

"""Импортируем random."""
from random import SystemRandom


def brain_progression():
    """Функция игры brain-progression.

    Returns:
        Dict: True если корректный ответ, иначе False.
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
    cryptogen = SystemRandom()
    rand_len_progression = cryptogen.randrange(5, 15)
    rand_step = cryptogen.randrange(1, 10)
    progression = list(map(str, range(rand_step,
                                      rand_len_progression * rand_step + 1,
                                      rand_step)))
    return progression


def get_random_element(progression):
    cryptogen = SystemRandom()
    rand_item = cryptogen.randrange(len(progression))
    random_element = progression[rand_item]
    return random_element
